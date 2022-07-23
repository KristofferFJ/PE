import requests as requests
from bs4 import BeautifulSoup

from new_problems_fetch.default_file_writer import write_default_text
from new_problems_fetch.title_fetch import problem_title

base_url = "https://projecteuler.net/problem="
problem_number = 700

soup = BeautifulSoup(requests.get(base_url + str(problem_number)).text, 'html.parser')
title = problem_title(soup)
write_default_text(soup, title)