import openai
from pathlib import Path
import json
import hashlib


LOCALES = [
    ('French', 'fr'),
#    ('German', 'de'),
#    ('Spanish', 'es'),
   ('Chinese', 'zh'),
]

# LOCALES = [
#     ('Dutch', 'nl'),
#     ('French', 'fr'),
#     ('Italian', 'it'),
#     ('Portuguese', 'pt'),
#     ('Cantonese', 'yue'),
#     ('Japanese', 'ja'),
#     ('Korean', 'ko'),
#     ('Indonesian', 'id'),
#     ('Hindi', 'hi'),
#     ('Bengali', 'bn'),
#     ('Arabic', 'ar'),
#     ('Hebrew', 'he'),
#     ('Russian', 'ru'),
#     ('Turkish', 'tr'),
# ]

SPECIAL_TERMS = [
    "sketchpad",
    "mouse_response",
    "keyboard_response",
    "sampler",
    "synth",
    "logger",
    "coroutines",
    "advanced_delay",
    "repeat_cycle",
    "inline_script",
    "inline_javascript",
    "form_base",
    "form_consent",
    "form_text_input",
    "form_text_display",
    "form_html"
]

SYSTEM = f'''You're a translator for OpenSesame, a program for developing psychology experiments. Do not translate: markup and tags, text in ALL_CAPS, technical terms, terms that have a special meaning within OpenSesame, such as: {', '.join(SPECIAL_TERMS)}, and other similar terms. Preserve markdown formatting, whitespace, capitalization, and punctuation. Text between `<notranslate>` tags should be preserved in the original language.

Reply with a %s translation. Only provide the translated text without adding any additional text. This concludes the instruction. The to be translated text will be provided next.'''
SYSTEM_API = f'''You're a translator for OpenSesame, a program for developing psychology experiments. Do not translate: markup and tags, text in ALL_CAPS, technical terms, terms that have a special meaning within OpenSesame, such as: {', '.join(SPECIAL_TERMS)}, and other similar terms. Preserve markdown formatting, whitespace, capitalization, and punctuation. Text between `<notranslate>` tags should be preserved in the original language.

Important: This text is an API documentation. Therefore, do not translate class names, function names, and parameter names.

Reply with a %s translation. Only provide the translated text without adding any additional text. This concludes the instruction. The to be translated text will be provided next.'''
MODEL = 'gpt-4'
openai.api_key = (Path.home() / '.openai-api-key').read_text().strip()
ROOT = Path('../content/pages')
INCLUDE = Path('../include')
MAX_SECTION_LENGTH = 4000
TRANSLATION_CACHE = Path('translations.json')
N_PROCESS = 20  # For multiprocessing

def consistent_hash(string):
    sha256 = hashlib.sha256()
    sha256.update(string.encode('utf-8'))
    hash_hex = sha256.hexdigest()
    return hash_hex


def parse_metadata(text):
    if '\n\n' in text:
        text = text[:text.find('\n\n')]
    text = text.replace('---', '').strip()
    metadata = {}
    for line in text.split('\n'):
        if not line:
            continue
        key, value = line.split(': ', 1)
        metadata[key.strip()] = value.strip()
    return metadata


def metadata_to_text(metadata):
    lines = []
    for key, value in metadata.items():
        lines.append(f"{key}: {value}")
    return '\n'.join(lines)


def translation_cache():
    if TRANSLATION_CACHE.exists():
        with TRANSLATION_CACHE.open() as fd:
            return json.load(fd)
    return {}


def translate_text(text, language, code, system=SYSTEM, lock=None,
                   force_retranslate=False):
    translations = translation_cache()
    if text not in translations:
        translations[text] = {}
    if code in translations[text] and not force_retranslate:
        print('Retrieving translation from cache')
        return translations[text][code]
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "system", "content": SYSTEM % language},
                  {"role": "user", "content": text}],
        request_timeout=600)
    reply = response['choices'][0]['message']['content']
    if lock is not None:
        lock.acquire()
    translations = translation_cache()
    if text not in translations:
        translations[text] = {}
    translations[text][code] = reply
    with TRANSLATION_CACHE.open('w') as fd:
        json.dump(translations, fd, ensure_ascii=False, indent=2)
    if lock is not None:
        lock.release()
    return reply
