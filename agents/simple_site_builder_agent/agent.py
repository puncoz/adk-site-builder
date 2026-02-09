# Purpose:
#   This file defines the root LLM for the website builder use case.
#   The agent takes a user's natural language prompt describing a simple website,
#   generates a complete HTML+CSS+JS webpage, and uses a tool to save it as a file.
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from google.adk.agents.llm_agent import Agent

from tools.file_writer_tool import write_to_file
from utils.file_loader import load_file

root_agent = Agent(
    # unique name for the agent; also shown in the UI
    name='simple_website_builder_agent',

    # id of gemini model used to generate responses
    model='gemini-2.5-flash',

    # a short summary of what agent does
    # it is loaded from file
    description=load_file(filename='agents/simple_site_builder_agent/prompts/description.txt'),

    # the prompt/instruction that tells agent what kind of behavior to exhibit
    # it is loaded from file
    instruction=load_file(filename='agents/simple_site_builder_agent/prompts/instructions.txt'),

    # a list of tools agent can invoke during execution,
    # in this case, just one: a function that writes generated HTML to a file
    tools=[write_to_file]
)
