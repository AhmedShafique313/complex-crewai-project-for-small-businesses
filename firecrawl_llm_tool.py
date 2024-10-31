import os
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import json

load_dotenv()
firecrawl_api_key = os.environ.get('FIRECRAWL_API_KEY')

def mapping_function():
    tool = FirecrawlApp(api_key=firecrawl_api_key)
    map_result = tool.map_url('designgaga.ca')
    with open('mapped_site.json', 'w') as f:
        json.dump(map_result, f, indent=4)
    return

def scrapping_function():
    app = FirecrawlApp(api_key=firecrawl_api_key)
    scrape_result = app.scrape_url('designgaga.ca', params={'formats': ['markdown']})
    # print(scrape_result)
    markdown_file = scrape_result['markdown']
    with open('scrapped_data.md', 'w', encoding='utf-8') as file:
        file.write(markdown_file)
    return
