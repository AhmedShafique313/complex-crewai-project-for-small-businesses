from firecrawl_llm_tool import mapping_function
from crews import crew1, crew2

def main():
    mapping_function()
    crew1.kickoff()
    crew2.kickoff()

if __name__ == '__main__':
    main()