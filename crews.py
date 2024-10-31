from crewai import Crew
from agents import file_reader
from task import file_reader_task

crew = Crew(
    agents=[file_reader],
    tasks=[file_reader_task],
    verbose=2
)