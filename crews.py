from crewai import Crew, Process
from agents import file_reader, icp_generator_agent
from task import file_reader_task, icp_generator_task

crew1 = Crew(
    agents=[file_reader],
    tasks=[file_reader_task],
    verbose=1,
)

crew2 = Crew(
    agents=[icp_generator_agent],
    tasks=[icp_generator_task],
    verbose=1,
)