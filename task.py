from crewai import Task
from agents import file_reader, icp_generator_agent

file_reader_task = Task(
    description='Read the scraped data JSON data and extract important information.',
    expected_output='Must add all these details Business Name, Industry, Services, Location, Contact Info, etc and save the entire data in the output file',
    agent=file_reader,
    output_file='basic_info.md'
)

icp_generator_task = Task(
    description='Read the data from the .md file and generates the ideal customer profile according to the industry related to the business also find the target audience',
    expected_output='Generate the Ideal Customer Profile from the data and only save the ICP data in the output file',
    agent=icp_generator_agent,
    output_file='icp_data.md',
)