import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from google.adk.agents import SequentialAgent

from agents.website_coder_agent.agent import website_coder_agent
from agents.website_designer_agent.agent import website_designer_agent
from agents.website_planner_agent.agent import website_planner_agent
from utils.file_loader import load_file

root_agent = SequentialAgent(
    name='multi_step_site_builder_agent',
    description=load_file(filename="agents/multi_step_site_builder_agent/description.txt"),
    sub_agents=[
        website_planner_agent,
        website_designer_agent,
        website_coder_agent
    ]
)
