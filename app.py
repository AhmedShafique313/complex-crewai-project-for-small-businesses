from firecrawl_llm_tool import mapping_function, scrapping_function
from crews import crew

def main():
    mapping_function()
    result = crew.kickoff()
    print(result)

if __name__ == '__main__':
    main()