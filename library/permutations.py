# Bibliotek med permutationsfunktioner
from typing import List


class Permutations:

    @staticmethod
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
                Permutations.add_permutations(permutations, new_numbers, new_rest)

    @staticmethod
    def permutations(number):
        s = str(number)
        number_list = []
        for char in s:
            number_list.append(char)
        permutation_list = []
        new_list = []
        Permutations.add_permutations(permutation_list, new_list, number_list)
        return permutation_list

    @staticmethod
    def combinations_of_length_3(word: str) -> List[str]:
        combinations = []
        for i in word:
            for j in word:
                for k in word:
                    combinations.append(i + j + k)
        return combinations