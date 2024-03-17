from __future__ import annotations

import json
from pathlib import Path

SRC = Path(__file__).parent.parent
DATA = SRC / "data" / "config.json"


def prompt_for_name() -> str:
    """Prompt the user for their name."""
    while True:
        name = input("What is your name? ")
        if name:
            return name


def persist_name(name: str, DATA: Path) -> None:
    """Persist the user's name to the config file."""
    with open(DATA, "r+") as f:
        data = json.load(f)
        data["name"] = name
    json.dump(data, open(DATA, "w"))


def validate_name(name: str) -> str:
    """Ensure the user's name is not empty, if it is, prompt for it and save it."""
    if not name:
        name = prompt_for_name()
        persist_name(name, DATA)

    return name


def retrieve_name(DATA: Path = DATA) -> str:
    """Retrieve the user's name from the config file."""
    with open(DATA, "r") as f:
        name = json.load(f)["name"]
    return validate_name(name)

