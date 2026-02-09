# Purpose:
#   Provides a utility function `load_file` that reads plain text from a file, typically used to load
#   prompts instructions or descriptions for LLM agents. If file is not found or unreadable, a default string
#   is returned.

# import `os` module for working with file paths and environment context
# not used here but common in loaders
import os

# Function: load_file
def load_file(filename: str, default: str = '') -> str:
    """
    Loads plain text for instructions and descriptions from a given file path.

    Args:
        filename (str): Path to the file to read (relative or absolute)
        default (str): Default string to return if file is not found or fails to load

    Returns:
        str: File contents if successful, or fallback default string.
    """

    try:
        # attempt to open file in read mode with utf-8 encoding
        # this ensures support for non-ascii characters in prompt files
        with open(filename, 'r', encoding="utf-8") as file:
            # read and return entire contents of file
            return file.read()

    except FileNotFoundError:
        # if file doesn't exist, log a warning and fall back to default value
        print(f"[WARNING] File not found: {filename}. Returning default string.")
        return default

    except Exception as exception:
        # catch any other exception (eg: permission issues, io errors) and log it
        print(f"[ERROR] Failed to load file: {filename}: {exception}")

    # return fallback default string if anything goes wrong
    return default
