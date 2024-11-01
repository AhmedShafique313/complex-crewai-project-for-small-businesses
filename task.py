from crewai import Task
from agents import file_reader, icp_generator_agent

file_reader_task = Task(
    description='Read the scraped data JSON data and extract important information.',
    expected_output='Must add all these details Business Name, Industry, Services, Location, Contact Info, etc and save the entire data in the output file',
    agent=file_reader,
    output_file='basic_info.md'
)

icp_generator_task = Task(
    description="""Generates the ideal customer profile for related to industry also make points:
    Demographics: Including title/role, experience level, geographic location, agency size etc.
    Professional Goals: Including faster sales, maximizing property value, client satisfaction etc.
    Pain Points: Including difficult to move listings, lack of visual appeal, limited time or expertise, higher costs etc.
    Buying Triggers: Including new listings, luxury or high-value homes, sellers market, price-reduction pressure etc.
    Value Proposition for Real Estate Agents: Including enhanced marketing materials, full-service staging etc.
    Customer Behavior: Including relationship-oriented, tech-savvy etc.
    Marketing Channels to Reach Them: Including email campaigns, linkedIn & facebook ads, industry events and networking.
    Make a format bullet points and sub-bullet points. 
    """,
    expected_output='Generate the Ideal Customer Profile from the data and only save the ICP data in the output file',
    agent=icp_generator_agent,
    output_file='icp_data.md',
)