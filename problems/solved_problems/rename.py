import os

from new_problems_fetch.title_fetch import format_title

print(f"Before Renaming: {os.listdir()}")
os.rename('geeks.txt', 'PythonGeeks.txt')
print(f"After Renaming: {os.listdir()}")
