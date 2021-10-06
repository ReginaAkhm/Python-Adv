"""
Дана строка с латинскими символами в нижнем регистре
Нужно вывести отсортированную последовательность всех уникальных подстрок
Пустая строка и строка целиком не учитываются

Пример: "students"
s t u d e n (t, s не учитываем)
st tu ud de en nt ts
и так далее
"""
from pprint import pprint

from more_itertools import windowed


def n_grams(word):
    result = []
    word = word.lower()
    for i in range(1, len(word)):
        i_grams = []
        anagram_temp = ["".join(w) for w in windowed(word, i)]
        for item in anagram_temp:
            if item not in i_grams:
                i_grams.append(item)
        result.append(i_grams)
    pprint(result)


if __name__ == '__main__':
    n_grams('students')
