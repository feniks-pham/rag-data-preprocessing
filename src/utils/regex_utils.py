import re
from typing import Dict, List, Tuple, Optional, Callable
from bs4 import BeautifulSoup

# Common regex patterns
RELATIVE_LINK_PATTERN = r'\]\(((?!http|mailto:|<)[^)#]+)(#[^\)]*)?\)'
GITBOOK_HINT_PATTERN = r'\{% hint style=".*?" %\}\n(.*?)\n\{% endhint %\}'
HTML_TABLE_PATTERN = r"<table.*?</table>"
FIGURE_IMAGE_PATTERN = r'<figure>\s*<img\s+src=["\'](?:\.\./)*\.gitbook/assets/([^"\']+)["\'].*?>\s*(?:<figcaption>.*?</figcaption>)?\s*</figure>'
EMPTY_ANCHOR_PATTERN = r'<a\s+href="[^"]*"\s+id="[^"]*"></a>'
GITBOOK_IMAGE_PATTERN = r'\[\]\(<(?:\.\./)*\.gitbook/assets/([^>]+)>\)'
MARK_TAG_PATTERN = r'<mark[^>]*>(.*?)</mark>'
SPACE_ENTITIES_PATTERN = r'&#x20;|&#xA0;|&nbsp;| '

def convert_relative_links(
    content: str, 
    file_path: str, 
    base_url: str = 'https://docs.vngcloud.vn/vng-cloud-document/vn',
    base_dir_pattern: str = r'^.*?/data/(?:vngcloud_docs|English)'
) -> str:
    """
    Convert relative links to absolute URLs.
    
    Args:
        content: Markdown content
        file_path: Path of the current file
        base_url: Base URL for absolute links
        base_dir_pattern: Pattern to match base directory
        
    Returns:
        str: Content with converted links
    """
    def replace_link(match: re.Match) -> str:
        relative_path, anchor = match.groups()
        anchor = anchor or ""
        
        from pathlib import Path
        absolute_path = (Path(file_path).parent / relative_path).resolve()
        absolute_path = re.sub(base_dir_pattern, base_url, str(absolute_path))
        
        if absolute_path.endswith("/README.md"):
            absolute_path = absolute_path.removesuffix("/README.md")
        else:
            absolute_path = absolute_path.removesuffix('.md')
            
        return f"]({absolute_path}{anchor})"
    
    return re.sub(RELATIVE_LINK_PATTERN, replace_link, content)

def convert_html_elements(html: str, tag_processors: Dict[str, Callable] = None) -> str:
    """
    Convert HTML elements to markdown using BeautifulSoup.
    
    Args:
        html: HTML content
        tag_processors: Dictionary of tag names to processor functions
        
    Returns:
        str: Converted markdown content
    """
    if tag_processors is None:
        tag_processors = {
            'strong': lambda tag: f"**{tag.text.strip()}**",
            'code': lambda tag: f"`{tag.text.strip()}`",
            'a': lambda tag: f"[{tag.text.strip()}]({tag.get('href', '#')})"
        }
    
    soup = BeautifulSoup(html, 'html.parser')
    
    for tag_name, processor in tag_processors.items():
        for tag in soup.find_all(tag_name):
            tag.replace_with(processor(tag))
    
    return soup.get_text(separator=' ').strip()

def convert_html_table(html: str) -> str:
    """
    Convert HTML table to markdown format.
    
    Args:
        html: HTML table content
        
    Returns:
        str: Markdown table
    """
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    if not table:
        return ""
    
    # Extract headers
    headers = [th.text.strip() for th in table.find_all('th')]
    if not headers:
        return ""
    
    # Create table structure
    header_row = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    
    # Convert rows
    rows = []
    for tr in table.find_all('tr')[1:]:
        row_data = [convert_html_elements(str(td)) for td in tr.find_all('td')]
        rows.append("| " + " | ".join(row_data) + " |")
    
    return "\n".join([header_row, separator] + rows)

def convert_gitbook_hints(content: str) -> str:
    """
    Convert GitBook hint blocks to markdown blockquotes.
    
    Args:
        content: Markdown content with GitBook hints
        
    Returns:
        str: Content with converted hints
    """
    def replace_hint(match: re.Match) -> str:
        hint_content = match.group(1).strip()
        return "\n".join(
            "> " + line if line.strip() else ">" 
            for line in hint_content.split("\n")
        )
    
    return re.sub(GITBOOK_HINT_PATTERN, replace_hint, content, flags=re.DOTALL)

def convert_images(
    content: str, 
    assets_base_url: str = "https://github.com/vngcloud/docs/blob/main/Vietnamese/.gitbook/assets"
) -> str:
    """
    Convert GitBook image references to markdown format.
    
    Args:
        content: Markdown content
        assets_base_url: Base URL for assets
        
    Returns:
        str: Content with converted image references
    """
    # Convert figure/image tags
    content = re.sub(
        FIGURE_IMAGE_PATTERN,
        lambda m: f"![Image]({assets_base_url}/{m.group(1).strip().replace(' ', '%20')}?raw=true)",
        content
    )
    
    # Convert image references
    content = re.sub(
        GITBOOK_IMAGE_PATTERN,
        lambda m: f"![Image]({assets_base_url}/{m.group(1).strip().replace(' ', '%20')}?raw=true)",
        content
    )
    
    return content

def clean_markdown(content: str) -> str:
    """
    Clean up markdown content by removing unnecessary elements and normalizing spaces.
    
    Args:
        content: Markdown content
        
    Returns:
        str: Cleaned markdown content
    """
    # Remove empty anchors
    content = re.sub(EMPTY_ANCHOR_PATTERN, '', content)
    
    # Convert mark tags to bold
    content = re.sub(MARK_TAG_PATTERN, r'**\1**', content, flags=re.DOTALL)
    
    # Normalize spaces
    content = re.sub(SPACE_ENTITIES_PATTERN, ' ', content)
    
    return content
