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
    return map_result