def write_default_text(soup, title: str):
    with open("../problems/unsolved_problems/" + title, "w") as new_file:
        content = soup.find(id='container').find(id='content')
        new_file.write("import unittest\n\n")
        new_file.write(_get_header(soup) + "\n")
        new_file.write('""" \n')
        new_file.write(_get_problem_content(content) + "\n")
        new_file.write('""" \n')
        new_file.write("\n")
        new_file.write("\n")
        new_file.write("class Test(unittest.TestCase):\n")
        new_file.write("    def test(self):\n")
        new_file.write("        pass\n")


def _get_header(content):
    return "# " + content.h2.text


def _get_problem_content(content):
    return "\n".join([tag.text for tag in content.find(role='problem').find_all('p')])

