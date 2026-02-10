import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from google.adk.agents import LlmAgent

from utils.file_loader import load_file

website_designer_agent = LlmAgent(
    name='website_designer_agent',
    model='gemini-2.5-flash',
    description=load_file(filename="agents/website_designer_agent/description.txt"),
    instruction=load_file(filename="agents/website_designer_agent/instructions.txt"),
    output_key="website_designer_agent_output"
)
