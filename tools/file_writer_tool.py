# Purpose:
#   This module defines a single tool function, `write_to_file`, which saves provided HTML/CSS/JS content to a
#   timestamped HTML file inside an output directory. This is used by agents to persist generated webpage content.

# import `datetime` module to generate a unique timestamp for filename
from datetime import datetime

# import `Path` from `pathlib` for convenient and safe file/directory handling
from pathlib import Path

from typing import TypedDict


# define shape of dictionary
class FileWriteStatus(TypedDict):
    status: str
    filename: str

# Tool Function: write_to_file
def write_to_file(content: str) -> FileWriteStatus:
    """
    Writes given HTML/CSS/JS content to a timestamped HTML file.

    Args:
       content (str): full HTML content as a string to be saved in file

    Returns:
         dict[str, str]: a dictionary containing status and generated filename
    """

    output_dir = "output"

    # get current date and time, format it as YYMMDD_HHMMSS
    # eg: 260210_142314
    timestamp = datetime.now().strftime("%y%m%d_%H%M%S")

    # construct output filename using timestamp
    # eg: output/index_260210_14231.html
    filename = f"{output_dir}/input_{timestamp}.html"

    # ensure "output" directory exists. if it doesn't, create it
    # `exist_ok=True` prevents an error if directory already exists.
    Path(output_dir).mkdir(exist_ok=True)

    # write HTML content to constructed file
    # `encoding='utf-8'` ensures proper character encoding
    Path(filename).write_text(content, encoding="utf-8")

    # returns a dictionary indicating success, and filename that was written
    return {
        "status": "success",
        "filename": filename
    }
