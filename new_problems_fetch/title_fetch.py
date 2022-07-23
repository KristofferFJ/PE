def problem_title(soup):
    raw_title = _get_title(soup)
    return format_title(raw_title)


def format_title(raw_title: str):
    title_without_hashtag = _remove_hashtag(raw_title)
    stripped_of_project_euler = _remove_project_euler(title_without_hashtag)
    without_space = _replace_spaces(stripped_of_project_euler)
    left_padded = _left_pad_zeros(without_space)
    test_prepended = _preprend_test(left_padded)
    return test_prepended.lower() + ".py"


def _get_title(soup):
    return soup.title.text


def _remove_hashtag(title: str):
    return title[1:]


def _remove_project_euler(title: str):
    return title.replace(" - Project Euler", "")


def _replace_spaces(title: str):
    return title.replace(" ", "_")


def _left_pad_zeros(title: str):
    problem_number_length = title.find("_")
    if problem_number_length == 3:
        return title
    elif problem_number_length == 2:
        return "0" + title
    elif problem_number_length == 1:
        return "00" + title
    else:
        raise Exception("wtf")


def _preprend_test(title: str):
    return "test_" + title
