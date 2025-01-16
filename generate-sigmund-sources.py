from pathlib import Path
import re
import openai
import json
from langchain.chat_models import ChatOpenAI
from datamatrix import functional as fnc
from publishconf import SITEURL


EXCLUDE = ['fr', 'zh', 'de', 'es']
INCLUDE = ['manual', 'items', 'beginner.md', 'intermediate.md',
           'intermediate-javascript.md']
SUMMARY_PROMPT_PATTERN = r"<summary_prompt>(.*?)</summary_prompt>"
OPENAI_API_KEY = (Path.home() / '.openai-api-key').read_text().strip()
DST = 'sigmund-sources-opensesame.jsonl'


@fnc.memoize(persistent=True)
def predict(query):
    llm = ChatOpenAI(model='gpt-4o', openai_api_key=OPENAI_API_KEY)
    answer = llm.predict(query)
    return answer


def write_document(doc, url, title):
    print(f'Writing {len(doc.split())} words')
    with open(DST, 'a') as fd:
        fd.write(json.dumps(
            {'content': f'# {title}\n\n{doc}', 
             'url': url,
             'title': title}) + '\n')        


def url_from_path(path):
    return '/'.join([SITEURL, '/'.join(path.parts[2:-1]), path.parts[-1][:-3]])
    
    
def title_from_content(content):
    for line in content.splitlines():
        if not line.startswith('title:'):
            continue
        return line[6:].strip().strip('"')
    raise ValueError('No title found in content')
    
    
def split_markdown_document(markdown_text, max_words=5000):
    # Split the text into lines
    lines = markdown_text.splitlines()

    # Prepare variables to hold the parts, the current part's words, and the word count
    parts = []
    current_part = []
    word_count = 0

    # Helper function to add the current part to parts
    def add_current_part():
        nonlocal current_part, parts, word_count
        if current_part:
            print(f'part word count: {word_count} {len("".join(current_part))}')
            parts.append('\n'.join(current_part))
            current_part = []
            word_count = 0

    # Iterate over all lines and split into parts by headings
    for line in lines:
        if line.startswith('#') and word_count > max_words:
            # If the line is a heading and we've exceeded the max word count,
            # start a new part
            add_current_part()

        current_part.append(line)
        word_count += len(line.split())

    # Add the last part if there's any content left
    add_current_part()

    return parts


if Path(DST).exists():
    Path(DST).unlink()
for path in Path('content/pages').glob('**/*.md'):
    if any(e in path.parts for e in EXCLUDE) or \
            not any(i in path.parts for i in INCLUDE):
        continue
    content = path.read_text()
    # Skip translated sources
    if 'locale:' in content:
        continue
    # Skip pages that should not be translated, because those tend to be
    # temporary workshop pages etc.
    if 'translate: false' in content:
        continue
    url = url_from_path(path)
    title = title_from_content(content)
    print('---')
    print(f'path: {path}')
    print(f'url: {url}')
    print(f'title: {title}')
    # A summary prompt can be embedded in the text in pseudo tags. If
    # so, then we use that to summarize the page, otherwise we use a
    # default summary tool. For chunks of text that are relatively
    # short, we don't summarize at all.
    match = re.search(SUMMARY_PROMPT_PATTERN, content, re.DOTALL)
    if match:
        summary_prompt = match.group(1).strip()
        text = re.sub(SUMMARY_PROMPT_PATTERN, '', content,
                      flags=re.DOTALL).strip()
        print(f'Document contains summary prompt')
        query = summary_prompt.format(content=text)
        summary = predict(query)
        if 'dummy' in summary:
            predict.clear()
            breakpoint()
            summary = predict(query)
        print(summary)
        write_document(summary, url, title)
    for chunk in split_markdown_document(content):
        write_document(chunk, url, title)

for path in Path('howtos').glob('**/*.md'):
    content = path.read_text()
    for howto in content.replace('# How to', '-*-# How to').split('-*-'):
        howto = howto.strip()
        if not howto:
            continue
        title, content = howto[2:].split('\n', maxsplit=1)
        write_document(howto, None, title)
