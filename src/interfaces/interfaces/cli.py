"""
CLI Interface

Provides:
- local terminal interaction
- recursive reasoning access
- operational diagnostics
- developer interaction tools
"""

import argparse
import json

from src.axios_core.core_engine import AxiosCore
from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()

# --------------------------------------------------
# Initialize AXIOS CORE
# --------------------------------------------------

axios_core = AxiosCore()

# --------------------------------------------------
# CLI Processing
# --------------------------------------------------

def process_prompt(prompt: str):
    """
    Process prompt through AXIOS CORE.
    """

    logger.info(
        f"CLI processing prompt: {prompt}"
    )

    result = axios_core.process(prompt)

    print(
        json.dumps(
            result,
            indent=2
        )
    )

# --------------------------------------------------
# Interactive Shell
# --------------------------------------------------

def interactive_shell():
    """
    Launch interactive recursive shell.
    """

    logger.info(
        "Launching interactive AXIOS shell."
    )

    print("\nAXIOS OS Interactive Shell")
    print("--------------------------------")
    print("Type 'exit' to quit.\n")

    while True:

        prompt = input("AXIOS > ")

        if prompt.lower() in ["exit", "quit"]:

            print("Shutting down AXIOS shell.")
            break

        result = axios_core.process(prompt)

        print(
            json.dumps(
                result,
                indent=2
            )
        )

# --------------------------------------------------
# CLI Entry Point
# --------------------------------------------------

def main():
    """
    Main CLI entry point.
    """

    parser = argparse.ArgumentParser(
        description=(
            "AXIOS OS Recursive "
            "Reasoning CLI"
        )
    )

    parser.add_argument(
        "--prompt",
        type=str,
        help="Prompt to process"
    )

    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Launch interactive shell"
    )

    args = parser.parse_args()

    # ----------------------------------------------
    # Interactive Mode
    # ----------------------------------------------

    if args.interactive:

        interactive_shell()

    # ----------------------------------------------
    # Single Prompt Mode
    # ----------------------------------------------

    elif args.prompt:

        process_prompt(args.prompt)

    else:

        parser.print_help()

# --------------------------------------------------
# Run CLI
# --------------------------------------------------

if __name__ == "__main__":

    main()
