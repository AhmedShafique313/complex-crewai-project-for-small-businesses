from firecrawl_llm_tool import mapping_function
from crews import crew1, crew2

def main():
    mapping_function()
    crew1.kickoff()
    result = crew2.kickoff()
    print(result)

if __name__ == '__main__':
    main()