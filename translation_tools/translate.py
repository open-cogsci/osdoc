from translation_utils import *
from pathlib import Path
import openai
import shutil
import time


def translate_page(target, language, code):
    t0 = time.time()
    src = ROOT / target
    dst = ROOT / code / target
    text = src.read_text()
    text_hash = hash(text)
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
        translation = translation.replace('\n<notranslate>', '\n%--')
        translation = translation.replace('\n</notranslate>', '\n--%')
        dst.write_text(translation)
    print(f'translation finished in {time.time() - t0:.1f}s')


def copy_images(target, code):
    src = ROOT / target
    dst = ROOT / code / target
    src_img = src.parent / 'img'
    dst_img = dst.parent / 'img'
    if dst_img.exists():
        shutil.rmtree(dst_img)
    shutil.copytree(src_img, dst_img)
    
    
for path in ROOT.glob('**/*.md'):
    target = path.relative_to(ROOT)
    if any(target.parts[0] == code for  language, code in LOCALES):
        continue
    for language, code in LOCALES:
        translate_page(target, language, code)
        copy_images(target, code)
