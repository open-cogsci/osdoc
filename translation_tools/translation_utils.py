import openai
from pathlib import Path
import json

LOCALES = [
    ('French', 'fr'),
]
# LOCALES = [
#     ('Dutch', 'nl'),
#     ('German', 'de'),
#     ('French', 'fr'),
#     ('Spanish', 'es'),
#     ('Italian', 'it'),
#     ('Portuguese', 'pt'),
#     ('Chinese', 'zh'),
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

SYSTEM = f'''You're a translator for OpenSesame, a program for developing psychology experiments. Do not translate: markup and tags, text in ALL_CAPS, technical terms, terms that have a special meaning within OpenSesame, such as: {', '.join(SPECIAL_TERMS)}, and other similar terms. Preserve markdown formatting, whitespace, capitalization, and punctuation.

Reply with a %s translation. Only provide the translated text without adding any additional text. This concludes the instruction. The to be translated text will be provided next.'''
MODEL = 'gpt-4'
openai.api_key = (Path.home() / '.openai-api-key').read_text().strip()
ROOT = Path('../content/pages')
MAX_SECTION_LENGTH = 4000
TRANSLATION_CACHE = Path('translations.json')
if TRANSLATION_CACHE.exists():
    with TRANSLATION_CACHE.open() as fd:
        translations = json.load(fd)
else:
    translations = {}


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


def translate_text(text, language, code, system=SYSTEM):
    if text not in translations:
        translations[text] = {}
    if code in translations[text]:
        print('retrieving translation from cache')
        return translations[text][code]
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "system", "content": SYSTEM % language},
                  {"role": "user", "content": text}])
    reply = response['choices'][0]['message']['content']
    translations[text][code] = reply
    with TRANSLATION_CACHE.open('w') as fd:
        json.dump(translations, fd, ensure_ascii=False, indent=2)
    return reply
