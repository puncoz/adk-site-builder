# Helper: Pretty print JSON objects using syntax coloring
import json
from typing import Any

from rich import print as rprint
from rich.syntax import Syntax


def print_json_response(response: Any, title: str) -> None:
    # displays a formatted and color-highlighted view of the JSON string by ADK response

    # section title
    print(f"\n=== {title} ===")

    try:
        # check if JSON string is wrapped by SDK
        if hasattr(response, "root"):
            data = response.root.model_dump(mode="json", exclude_none=True)
        else:
            data = response.model_dump(mode="json", exclude_none=True)

        # convert dict to pretty JSON string
        json_str = json.dumps(
            data,
            indent=2,
            ensure_ascii=False
        )
        syntax = Syntax(
            json_str,
            "json",
            theme="monokai",
            line_numbers=False
        )
        # print it with color
        rprint(syntax)

    except Exception as exception:
        # print fallback text if something fails
        rprint(f"[red bold]Error printing JSON: [/red bold] {exception}")
        rprint(repr(response))
