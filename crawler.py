import requests
from bs4 import BeautifulSoup


tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']

# Open file in append mode with UTF-8 encoding
with open('text.txt', 'a', encoding='utf-8') as f:
    url = 'https://docs.nvidia.com/cuda/'
    request = requests.get(url)

    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        body = soup.body

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
            '''
            elif tag.name == 'span':
                f.write(tag.get_text(strip=True) + '\n\n')
            '''

        # Traverse and process the HTML elements
        for element in body.descendants:
            if element.name in tags:
                process_and_write(element, f)
    else:
        print(f"Failed to retrieve the website. Status code: {request.status_code}")
