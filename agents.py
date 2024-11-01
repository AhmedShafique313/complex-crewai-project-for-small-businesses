from crewai import Agent
from firecrawl_llm_tool import scrapping_function
from icp_tool import icp_reader
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="llama3.2:1b",
    base_url="http://localhost:11434/v1"
)

info = scrapping_function('designgaga.ca')
icp_info = icp_reader()

file_reader = Agent(
    role='Senior JavaScript Object Notation Data Reader',
    goal=f'Effectively the entire read json data from {info} and extract important information',
    backstory="""You are a expert json data reader.""",
    tools=[],
    verbose=True,
    llm = llm
)

icp_generator_agent = Agent(
    role='Senior ICP Generator Agent',
    goal = f'Read the data from {icp_info} and generates the efficient ICP (Ideal Customer Profile) for the business',
    backstory="""You are an expert data reader and icp generator""",
    verbose=True,
    llm=llm
)
