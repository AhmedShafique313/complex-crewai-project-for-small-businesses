from firecrawl_llm_tool import mapping_function, scrapping_function
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="llama3.2:1b",
    base_url="http://localhost:11434/v1"
)

def main():
    mapping_function()
    scrapping_function()

if __name__ == '__main__':
    main()