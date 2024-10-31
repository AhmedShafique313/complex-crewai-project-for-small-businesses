from crewai import Agent
from firecrawl_llm_tool import scrapping_function
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="llama3.2:1b",
    base_url="http://localhost:11434/v1"
)

info = scrapping_function('designgaga.ca')

file_reader = Agent(
    role='Senior JavaScript Object Notation Data Reader',
    goal=f'Effectively the entire read json data from {info} and extract important information',
    backstory="""You are a expert json data reader.""",
    tools=[],
    verbose=True,
    llm = llm
)
