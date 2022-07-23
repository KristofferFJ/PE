import os
from typing import Set

import requests as requests
from bs4 import BeautifulSoup

from new_problems_fetch.default_file_writer import write_default_text
from new_problems_fetch.existing_problems_finder import get_existing_problems
from new_problems_fetch.title_fetch import problem_title

base_url = "https://projecteuler.net/problem="
existing_problems: Set[int] = get_existing_problems()

problem_number = 1
while True:
    if problem_number in existing_problems:
        problem_number += 1
        continue
    soup = BeautifulSoup(requests.get(base_url + str(problem_number)).text, 'html.parser')
    if len(soup.contents) == 0:
        break
    title = problem_title(soup)
    print("Creating test: " + title)
    write_default_text(soup, title)
    problem_number += 1
