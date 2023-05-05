from translation_utils import *
from pathlib import Path
import openai
import shutil
import difflib
import time
import sys
import multiprocessing as mp
import itertools as it
import argparse


def translate_page(target, root, language, code, interactive=False, lock=None,
                   has_info=True, system=None, force_retranslate=False):
    """Translates a page.

    Parameters
    ----------
    target: str or Path
    root: Path
    language: str
    code: str
    interactive: bool, optional
        Indicates whether the user is asked to confirm overwriting of
        translations.
    lock: Lock or None, optional
        A lock for multiprocessing
    has_info: bool, optional
        Indicates whether the page starts with a metadata block.
    system: str or None, optional
        The system prompt.
    """
    t0 = time.time()
    src = root / target
    dst = root / code / target
    # Release notes can be very long because of the package list. Therfore we
    # don't translate old notes
    if target.is_relative_to('notes') and \
            target.parts[-1][0] in ('2', '3', '0'):
        print(f'Not translating old release note {dst}')
        dst.parent.mkdir(exist_ok=True)
        dst.write_text(src.read_text())
        return
    # If we're not in interactive mode, we assume that existing translations
    # are fine (i.e. we don't offer to retranslate)
    if dst.exists() and not interactive and not force_retranslate:
        print(f'File {dst} already exists. Skipping')
        return
    text = src.read_text()
    print(f'Translating {src} to {language} using {MODEL} (n_words: {len(text)})')
    text_hash = consistent_hash(text)
    if has_info:
        info, text = text.split('\n\n', 1)
        # Update info
        info = parse_metadata(info)
        # Some (old) pages are excluded from translation because this is not
        # necessary
        if info.get('translate', True) in (False, 'false'):
            print(f'Page should not be translated')
            return
        info['hash'] = text_hash
        info['locale'] = code
        info['language'] = language
        # Translate the title from YAML info
        print(f'Original title: {info["title"]}')
        info['title'] = translate_text(info['title'], language, code,
                                       lock=lock, system=system,
                                       force_retranslate=force_retranslate)
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
    translated_sections = [info] if has_info else []
    for i, section in enumerate(sections):
        translated_section = translate_text(section, language, code, lock=lock,
                                            force_retranslate=force_retranslate)
        translated_sections.append(translated_section)
        print(f'* Translated section {i + 1} / {len(sections)} (n_words: {len(section)} -> {len(translated_section)})')
    # Write the translations to file. We do this continuously so that we
    # can monitor the progress if necessary.
    dst.parent.mkdir(parents=True, exist_ok=True)
    translation = '\n\n'.join(translated_sections)
    translation = translation.replace('<notranslate>[TOC]</notranslate>', '[TOC]')
    translation = translation.replace('\n<notranslate>', '\n%--')
    translation = translation.replace('\n</notranslate>', '\n--%')
    # If a translation already exists but is different from the current
    # translation, then we ask the user what to do.
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
    dst.parent.mkdir(exist_ok=True)
    dst.write_text(translation)
    print(f'translation finished in {time.time() - t0:.1f}s')


def copy_resources(target, root, resource, code, lock=None):
    """Copies the resource folder from the base documentation to the translated
    documentation.
    """
    if lock is not None:
        lock.acquire()
    src = root / target
    dst = root / code / target
    src_img = src.parent / resource
    if src_img.exists():
        dst_img = dst.parent / resource
        if dst_img.exists():
            shutil.rmtree(dst_img)
        shutil.copytree(src_img, dst_img)
    if lock is not None:
        lock.release()


def mp_translate(target, root, language, code, lock, has_info, system,
                 force_retranslate):
    """A simple wrapper function for the multiprocessing module"""
    translate_page(target, root, language, code, lock=lock, has_info=has_info,
                   system=system, force_retranslate=force_retranslate)
    copy_resources(target, root, 'img', code, lock=lock)
    copy_resources(target, root, 'lst', code, lock=lock)
    copy_resources(target, root, 'tbl', code, lock=lock)


def main_multiprocessing(locales, select_path, force_retranslate):
    """Performs a full translation using multiple processes. This ignores
    existing translations, regardless of their content.
    """
    args = []
    manager = mp.Manager()
    lock = manager.Lock()
    for language, code in LOCALES:
        if locales and code not in locales:
            continue
        for path in it.chain(ROOT.glob('**/*.md'), INCLUDE.glob('**/*.md')):
            # If a specific path is specified, only process that path
            if select_path and Path(select_path).absolute() != path.absolute():
                continue
            if path.is_relative_to(ROOT):
                target = path.relative_to(ROOT)
                root = ROOT
                has_info = True
                system = SYSTEM
            else:
                target = path.relative_to(INCLUDE)
                root = INCLUDE
                has_info = False
                system = SYSTEM_API
            if any(target.parts[0] == code for language, code in LOCALES):
                continue
            args.append([target, root, language, code, lock, has_info, system,
                         force_retranslate])
    with mp.Pool(N_PROCESS) as pool:
        pool.starmap(mp_translate, args)
        

def main(locales, select_path, force_retranslate):
    """Performs a full translation is a single process. This also prompts the
    user for what to do with existing but non-matching translations.
    """
    for language, code in LOCALES:
        # If a locale is specified, only process that locale
        if locales and code not in locales:
            continue
        for path in it.chain(ROOT.glob('**/*.md'), INCLUDE.glob('**/*.md')):
            # If a specific path is specified, only process that path
            if select_path and Path(select_path).absolute() != path.absolute():
                continue
            if path.is_relative_to(ROOT):
                target = path.relative_to(ROOT)
                root = ROOT
                has_info = True
                system = SYSTEM
            else:
                target = path.relative_to(INCLUDE)
                root = INCLUDE
                has_info = False
                system = SYSTEM_API
            if any(target.parts[0] == code for language, code in LOCALES):
                continue
            translate_page(target, root, language, code, interactive=True,
                           has_info=has_info, system=system,
                           force_retranslate=force_retranslate)
            copy_resources(target, root, 'img', code)
            copy_resources(target, root, 'lst', code)
            copy_resources(target, root, 'tbl', code)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--multiprocessing', action='store_true',
                        help='Use multiprocessing')
    parser.add_argument('--locales', action='store',
                        help='A comma-separated list of language codes')
    parser.add_argument('--path', action='store',
                        help='A path to a specific file to be translated')
    parser.add_argument('--force-retranslate', action='store_true',
                        help='Retriggers a translation even if a file has '
                             'already been translated')
    args = parser.parse_args()
    if args.multiprocessing:
        main_multiprocessing(args.locales, args.path, args.force_retranslate)
    else:
        main(args.locales, args.path, args.force_retranslate)
