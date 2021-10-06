# Анаграммы*
# Задается словарь (список слов).
# Найти в нем все анаграммы (слова, составленные из одних и тех же букв).
# Пример: 'hello' <-> 'ollhe'
import itertools
from pprint import pprint


def make_anagram_dict(line):
    d = {}
    for word in line:
        word = word.lower()
        key = ''.join(sorted(word))
        anagram_temp = list(itertools.permutations(key))
        anagram = []
        for i in anagram_temp:
            i = ''.join(i)
            anagram.append(i)
        d[key] = anagram
    return d


if __name__ == '__main__':
    my_list = ['hello', 'table', 'count']
    pprint(make_anagram_dict(my_list))
