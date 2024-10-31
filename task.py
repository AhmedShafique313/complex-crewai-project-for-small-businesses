from crewai import Task
from agents import file_reader

file_reader_task = Task(
    description='Read the scraped data JSON data and extract important information.',
    expected_output='Business Name, Industry, Services, Location, Contact Info, etc.',
    agent=file_reader,
    output_file='basic_info.md'
)