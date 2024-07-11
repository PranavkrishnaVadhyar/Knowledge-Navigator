import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to process and write text based on tag type
def process_and_write(tag, f):
    if tag.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        heading_level = tag.name
        if heading_level == 'h1':
            f.write('\n\n# ' + tag.get_text(strip=True) + '\n\n')
        elif heading_level == 'h2':
            f.write('\n\n## ' + tag.get_text(strip=True) + '\n\n')
        elif heading_level == 'h3':
            f.write('\n\n### ' + tag.get_text(strip=True) + '\n\n')
        elif heading_level == 'h4':
            f.write('\n\n#### ' + tag.get_text(strip=True) + '\n\n')
        elif heading_level == 'h5':
            f.write('\n\n##### ' + tag.get_text(strip=True) + '\n\n')
        elif heading_level == 'h6':
            f.write('\n\n###### ' + tag.get_text(strip=True) + '\n\n')
    elif tag.name == 'p':
        f.write(tag.get_text(strip=True) + '\n\n')


# Function to recursively scrape and collect sublinks
def scrape_page(url, depth, max_depth, f, visited, tree):
    if depth > max_depth or url in visited:
        return
    
    visited.add(url)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        
        soup = BeautifulSoup(response.content, 'html.parser')
        body = soup.body
        
        if body is None:
            print(f"No body tag found in {url}")
            return
        
        # Traverse and process the HTML elements
        for element in body.descendants:
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']:
                process_and_write(element, f)
        
        # Collect sublinks
        for link in soup.find_all('a', href=True):
            full_url = urljoin(url, link['href'])
            if full_url not in visited:
                if url not in tree:
                    tree[url] = []
                tree[url].append(full_url)
                scrape_page(full_url, depth + 1, max_depth, f, visited, tree)
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while processing {url}: {e}")

# Open file in append mode with UTF-8 encoding
with open('text.txt', 'a', encoding='utf-8') as f:
    start_url = 'https://docs.nvidia.com/cuda/'
    max_depth = 5
    visited = set()
    link_tree = {}
    
    # Start the scraping process
    scrape_page(start_url, 1, max_depth, f, visited, link_tree)
    
    # Print the link tree for debugging
    print("Link Tree:")
    for parent, children in link_tree.items():
        print(f"{parent}:")
        for child in children:
            print(f"  - {child}")
