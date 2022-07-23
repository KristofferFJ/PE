import os
from typing import Set


def get_existing_problems() -> Set[int]:
    return _get_problems("solved_problems").union(_get_problems("unsolved_problems"))


def _get_problems(type: str) -> Set[int]:
    return set([_filename_to_int(file) for file in os.listdir("../problems/" + type) if file.startswith("test")])


def _filename_to_int(filename: str) -> int:
    return int(_remove_prepended_0(filename[5:8]))


def _remove_prepended_0(integer_string: str) -> str:
    if integer_string[0] == 0:
        return _remove_prepended_0(integer_string[1:])
    return integer_string
