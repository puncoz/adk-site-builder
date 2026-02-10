import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from google.adk.agents import LlmAgent

from utils.file_loader import load_file
from tools.file_writer_tool import write_to_file

website_coder_agent = LlmAgent(
    name='website_coder_agent',
    model='gemini-2.5-flash',
    description=load_file(filename="agents/website_coder_agent/description.txt"),
    instruction=load_file(filename="agents/website_coder_agent/instructions.txt"),
    tools=[write_to_file]
)
