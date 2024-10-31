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

def scrapping_function(website_url):
    app = FirecrawlApp(api_key=firecrawl_api_key)
    specific_pages = [
        website_url,  # Main page
        f"{website_url}/about-us",
        f"{website_url}/services",
        f"{website_url}/careers",
        f"{website_url}/portfolio",
        f"{website_url}/contact"
    ]
    scraped_data = {}
    for page in specific_pages:
        scrape_result = app.scrape_url(page, params={'formats': ['markdown']})
        scraped_data[page] = scrape_result.get('markdown', 'No content available')
    with open('scraped_data.json', 'w', encoding='utf-8') as md_file:
        json.dump(scraped_data, md_file, ensure_ascii=False, indent=4)
    # scrape_result1 = app.scrape_url('designgaga.ca', params={'formats': ['markdown']})
    # scrape_result2 = app.scrape_url('https://designgaga.ca/contact', params={'formats': ['markdown']})
    # markdown_file = scrape_result1['markdown'] + "\n\n---\n\n" + scrape_result2['markdown']
    # with open('scrapped_data.md', 'w', encoding='utf-8') as file:
    #     file.write(markdown_file)
    return
