from translation_utils import *
from pathlib import Path
import openai
import shutil
import difflib
import time
import multiprocessing as mp


def translate_page(target, language, code):
    """Translates a page.
    
    Parameters
    ----------
    target: str or Path
    language: str
    code: str
    """
    t0 = time.time()
    src = ROOT / target
    dst = ROOT / code / target
    text = src.read_text()
    text_hash = consistent_hash(text)
    info, text = text.split('\n\n', 1)
    # Update info
    info = parse_metadata(info)
    info['hash'] = text_hash
    info['locale'] = code
    info['language'] = language
    print(f'Translating {src} to {language} using {MODEL} (n_words: {len(text)})')
    # Translate the title from YAML info
    print(f'Original title: {info["title"]}')
    info['title'] = translate_text(info['title'], language, code)
    print(f'Translated title: {info["title"]}')
    info = metadata_to_text(info)
    # Make sure that academicmarkdown blocks aren't translated
    text = text.replace('\n%--', '\n<notranslate>')
    text = text.replace('\n--%', '\n</notranslate>')
    text = text.replace('[TOC]', '<notranslate>[TOC]</notranslate>')
    # Split the text up into sections that are sufficiently short
    sections = []
    current_section = None
    for section in text.split('\n\n'):
        if current_section is None:
            current_section = section
        elif len(current_section) + len(section) > MAX_SECTION_LENGTH:
            sections.append(current_section)
            current_section = section
        else:
            current_section += '\n\n' + section
    if current_section:
        sections.append(current_section)
    # Translate the sections one by one
    translated_sections = [info]
    for i, section in enumerate(sections):
        translated_section = translate_text(section, language, code)
        translated_sections.append(translated_section)
        print(f'* translated section {i + 1} / {len(sections)} (n_words: {len(section)} -> {len(translated_section)})')
    # Write the translations to file. We do this continuously so that we
    # can monitor the progress if necessary.
    dst.parent.mkdir(parents=True, exist_ok=True)
    translation = '\n\n'.join(translated_sections)
    translation = translation.replace('<notranslate>[TOC]</notranslate>', '[TOC]')
    translation = translation.replace('\n<notranslate>', '\n%--')
    translation = translation.replace('\n</notranslate>', '\n--%')
    
    if dst.exists():
        current_translation = dst.read_text()
        if current_translation == translation:
            return
        print('*** DIFFSTART')
        diff = difflib.unified_diff(current_translation.splitlines(),
                                    translation.splitlines())
        for line in diff:
            print(line)
        print('*** DIFFEND')
        resp = input('>>> This page has been modified. Do you want to '
                     'overwrite the translation (y) or keep the '
                     'modifications (n)?')
        if resp != 'y':
            print('Keeping modifications')
            return
        print('Overwriting translation')
    dst.write_text(translation)
    print(f'translation finished in {time.time() - t0:.1f}s')


def copy_images(target, code):
    """Copies the img folder from the base documentation to the translated
    documentation.
    """
    src = ROOT / target
    dst = ROOT / code / target
    src_img = src.parent / 'img'
    dst_img = dst.parent / 'img'
    if dst_img.exists():
        shutil.rmtree(dst_img)
    shutil.copytree(src_img, dst_img)


def mp_translate(args):
    """A simple wrapper function for the multiprocessing module"""
    target, language, code = args
    translate_page(target, language, code)
    copy_images(target, code)


args = []
for language, code in LOCALES:
    for path in ROOT.glob('**/*.md'):
        target = path.relative_to(ROOT)
        if any(target.parts[0] == code for language, code in LOCALES):
            continue
        args.append([target, language, code])
with mp.Pool(10) as pool:
    pool.map(mp_translate, args)
