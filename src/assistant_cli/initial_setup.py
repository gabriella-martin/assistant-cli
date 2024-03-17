from __future__ import annotations

import json
from pathlib import Path

from simple_term_menu import TerminalMenu

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


def favourite_colour() -> str:
    """Prompt the user for their favourite colour."""
    options = [
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "purple",
        "cyan",
        "white",
        "gray",
    ]
    terminal_menu = TerminalMenu(
        options,
        title="What do you want your colour theme to be?",
        menu_cursor="> ",
        menu_cursor_style=("fg_black",),
    )
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]


def persist_favourite_colour(colour: str, DATA: Path) -> None:
    """Persist the user's favourite colour to the config file."""
    with open(DATA, "r+") as f:
        data = json.load(f)
        data["colour"] = colour
    json.dump(data, open(DATA, "w"))


def retrieve_favourite_colour(DATA: Path = DATA) -> str:
    """Retrieve the user's favourite colour from the config file."""
    with open(DATA, "r") as f:
        colour = json.load(f)["colour"]
    if not colour:
        colour = favourite_colour()
        persist_favourite_colour(colour, DATA)
    return colour
