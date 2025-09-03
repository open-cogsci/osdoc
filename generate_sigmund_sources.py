"""
Documentation parser for creating JSON files from Pelican site content.
Processes markdown files, extracts metadata, determines topics, and chunks content.
"""

from pathlib import Path
import re
import json
import tiktoken
from typing import List, Dict
from sigmund import static
from datamatrix import functional as fnc
from publishconf import SITEURL


# Configuration
EXCLUDE_DIRS = ['fr', 'zh', 'de', 'es']
INCLUDE_DIRS = ['manual', 'items', 'beginner.md', 'intermediate.md',
                'intermediate-javascript.md']
SUMMARY_PROMPT_PATTERN = r"<summary_prompt>(.*?)</summary_prompt>"
MAX_TOKENS = 8000  # Maximum tokens per chunk
OUTPUT_FILE = 'sigmund/opensesame.json'
COLLECTION = 'opensesame'
DEFAULT_TOPIC = 'opensesame'
# Secondary topics that can be detected
SECONDARY_TOPICS = {
    'datamatrix': 'Data analysis and manipulation with DataMatrix',
    'inline_script': 'Python inline scripting in OpenSesame',
    'inline_javascript': 'JavaScript for OSWeb experiments'
}
FOUNDATION_DOCUMENTS = {
    'opensesame' : 'sigmund/opensesame.md',
    'inline_script': 'sigmund/inline_script.py',
    'inline_javascript': 'sigmund/inline_javascript.js',
}
EXTRA_DOCUMENTS = []
MODEL = 'gpt-5'

# Initialize tokenizer for GPT models
tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")


def process_includes(content: str, base_path: Path) -> str:
    """
    Process include directives in the content.
    Replace %-- include: path/to/file.md --% with the actual file content.
    Handles flexible YAML spacing around the colon.
    """
    # More flexible pattern that handles any whitespace around the colon
    include_pattern = r'%--\s*include\s*:\s*(.*?)\s*--%'
    
    def replace_include(match):
        include_path = match.group(1).strip()
        # Resolve the path relative to the content directory
        full_path = base_path / include_path
        
        try:
            if full_path.exists():
                included_content = full_path.read_text()
                # Recursively process includes in the included file
                print(f"Including file {full_path}")
                return process_includes(included_content, base_path)
            else:
                print(f"Warning: Include file not found: {full_path}")
                return match.group(0)  # Keep original if file not found
        except Exception as e:
            print(f"Error including file {full_path}: {e}")
            return match.group(0)
    
    return re.sub(include_pattern, replace_include, content)


@fnc.memoize(persistent=True)
def detect_secondary_topic(content: str, title: str) -> List[str]:
    """
    Use LLM to detect the most appropriate secondary topic for a page.
    """
    # Skip if no secondary topics are defined
    if not SECONDARY_TOPICS:
        return []
    
    # Build the topic descriptions dynamically
    topic_descriptions = '\n'.join([
        f"- {topic}: {description}"
        for topic, description in SECONDARY_TOPICS.items()
    ])    
    prompt = f"""Given the following documentation page title and content, determine which secondary topic(if any) is most appropriate.

Title: {title}

Content excerpt:
{content[:2000]}  # Use first 2000 chars as sample

Available secondary topics:
{topic_descriptions}

Reply with ONLY a comma-separated list of all topic names that clearly apply, or 'none' if no secondary topic is appropriate."""
    
    response = static.predict(prompt, model=MODEL).strip().lower()
    
    # Parse the response and filter valid topics
    topics = []
    for topic in response.split(','):
        topic = topic.strip()
        if topic in SECONDARY_TOPICS:
            topics.append(topic)
    
    return topics


def count_tokens(text: str) -> int:
    """Count the number of tokens in a text string."""
    return len(tokenizer.encode(text))


def chunk_markdown_by_tokens(text: str, max_tokens: int = MAX_TOKENS) -> List[str]:
    """
    Split markdown text into chunks based on token count, respecting markdown structure.
    """
    lines = text.splitlines()
    chunks = []
    current_chunk = []
    current_tokens = 0
    
    for line in lines:
        line_tokens = count_tokens(line + '\n')
        
        # If adding this line would exceed the limit and we're at a heading
        if current_tokens + line_tokens > max_tokens and current_chunk:
            # If it's a heading, start a new chunk
            if line.startswith('#'):
                chunks.append('\n'.join(current_chunk))
                current_chunk = [line]
                current_tokens = line_tokens
            else:
                # Otherwise, add the line anyway but start a new chunk after
                current_chunk.append(line)
                chunks.append('\n'.join(current_chunk))
                current_chunk = []
                current_tokens = 0
        else:
            current_chunk.append(line)
            current_tokens += line_tokens
    
    # Add the last chunk
    if current_chunk:
        chunks.append('\n'.join(current_chunk))
    
    return chunks


def extract_metadata(path: Path, content: str) -> Dict[str, any]:
    """Extract metadata from a markdown file."""
    # Extract title
    title = None
    for line in content.splitlines():
        if line.startswith('title:'):
            title = line[6:].strip().strip('"')
            break
    
    if not title:
        raise ValueError(f'No title found in {path}')
    
    # Generate URL
    url_parts = [SITEURL] + list(path.parts[2:-1]) + [path.parts[-1][:-3]]
    url = '/'.join(url_parts)
    
    return {
        'title': title,
        'url': url,
        'path': str(path),
    }


def should_skip_file(path: Path, content: str) -> bool:
    """Determine if a file should be skipped based on exclusion rules."""
    # Check if in excluded directories
    if any(exc in path.parts for exc in EXCLUDE_DIRS):
        return True
    
    # Check if not in included paths
    if not any(inc in str(path) for inc in INCLUDE_DIRS):
        return True
    
    # Skip translated content
    if 'locale:' in content:
        return True
    
    # Skip non-translatable content
    if 'translate: false' in content:
        return True
    
    return False


def create_document(content: str, metadata: Dict[str, any]) -> Dict[str, any]:
    """Create a document dictionary."""
    return {
        'content': content,
        **metadata
    }


def main():
    """Main processing function."""
    # List to collect all documents
    documents = []
    
    # Process all markdown files
    for path in Path('content/pages').glob('**/*.md'):
        content = path.read_text()
        
        # Skip files based on exclusion rules
        if should_skip_file(path, content):
            continue
        
        print(f'\n--- Processing: {path} ---')
        
        # Process include directives
        content = process_includes(content, Path('.'))
        
        # Extract basic metadata
        metadata = extract_metadata(path, content)
        print(f"Title: {metadata['title']}")
        print(f"URL: {metadata['url']}")
        
        # Determine topics
        topics = [DEFAULT_TOPIC]
        
        # Detect secondary topics if any are defined
        if SECONDARY_TOPICS:
            secondary_topics = detect_secondary_topic(content, metadata['title'])
            if secondary_topics:
                topics += secondary_topics
                print(f"Secondary topics detected: {secondary_topics}")
        
        metadata['topics'] = topics
        metadata['collection'] = COLLECTION
        metadata['foundation'] = False
        metadata['howto'] = False
        
        # Chunk the content
        chunks = chunk_markdown_by_tokens(content)
        print(f"Split into {len(chunks)} chunks")
        
        # Create document for each chunk
        for i, chunk in enumerate(chunks):
            chunk_metadata = metadata.copy()
            chunk_metadata['chunk'] = i + 1
            chunk_metadata['total_chunks'] = len(chunks)
            
            # Add title to chunk content
            chunk_content = f"# {metadata['title']}\n\n{chunk}"
            
            documents.append(create_document(chunk_content, chunk_metadata))
            print(f"  Chunk {i+1}: {count_tokens(chunk_content)} tokens")
            
        
    # Process foundation documents
    for topic, path in FOUNDATION_DOCUMENTS.items():
        metadata = {
            'title': f'Foundation document for {topic}',
            'collection': COLLECTION,
            'topic': topic,
            'howto': False,
            'foundation': True
        }
        documents.append(create_document(Path(path).read_text(), metadata))
        
    # Process extra documents:
    for metadata in EXTRA_DOCUMENTS:
        path = metadata.pop('path')
        metadata['collection'] = COLLECTION
        metadata['howto'] = False
        metadata['foundation'] = False
        metadata['topics'] = [DEFAULT_TOPIC]
        documents.append(create_document(Path(path).read_text(), metadata))    
    print(f"\nTotal extra documents: {len(documents)}")
    
    # Process how-to documents
    print("\n--- Processing how-to documents ---")
    for path in Path('howtos').glob('**/*.md'):
        content = path.read_text()
        
        # Process includes in how-to files too
        content = process_includes(content, path.parent)
        
        # Split into individual how-tos
        howtos = content.replace('# How to', '-*-# How to').split('-*-')
        
        for howto in howtos:
            howto = howto.strip()
            if not howto:
                continue
            
            title, howto_content = howto[2:].split('\n', maxsplit=1)
            
            # Create metadata for how-to
            metadata = {
                'title': title,
                'topics': [DEFAULT_TOPIC],
                'collection': COLLECTION,
                'howto': True,
                'source': 'howtos',
                'foundation': False
            }
            
            # Chunk if necessary
            chunks = chunk_markdown_by_tokens(howto)
            
            for i, chunk in enumerate(chunks):
                chunk_metadata = metadata.copy()
                if len(chunks) > 1:
                    chunk_metadata['chunk'] = i + 1
                    chunk_metadata['total_chunks'] = len(chunks)
                
                documents.append(create_document(chunk, chunk_metadata))
    
    # Write all documents to JSON file
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(documents, f, indent=2)
    
    print(f"\nProcessing complete! {len(documents)} documents written to {OUTPUT_FILE}")


if __name__ == '__main__':
    main()