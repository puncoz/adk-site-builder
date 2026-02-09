# import `simple_site_builder_agent` submodule from current `agents` package
# this triggers execution of `agents/simple_site_builder_agent/__init__.py`,
# which in turn typically loads or exposes the agent defined in `agent.py`
from . import agent
