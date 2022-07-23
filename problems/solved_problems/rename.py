import os

from new_problems_fetch.title_fetch import format_title

for file in os.listdir():
    if file.startswith("test") or file.startswith("rename") or file.startswith("__"):
        continue
    new_file_name = format_title(file)[0:-3].replace("_-", "")
    os.rename(file, new_file_name)
