# Bibliotek med permutationsfunktioner


def add_permutations(permutations, numbers, rest):
    if len(rest) == 1:
        final_list = list(numbers)
        final_list.append(rest[0])
        permutations.append(final_list)
    else:
        for i in range(len(rest)):
            new_rest = list(rest)
            new_numbers = list(numbers)
            new_numbers.append(rest[i])
            new_rest.pop(i)
            add_permutations(permutations, new_numbers, new_rest)


def permutations(number):
    s = str(number)
    number_list = []
    for char in s:
        number_list.append(char)
    permutation_list = []
    new_list = []
    add_permutations(permutation_list, new_list, number_list)
    return permutation_list


if __name__ == '__main__':
    print(permutations(765))
