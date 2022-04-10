from typing import Any


def find(lst: list, c: Any) -> list[int]:

    finalstr = ''

    for item in lst:
        if item == c:
            finalstr += item

    return [lst.index(item) for item in lst if c == item]


ints = [0, 1, 2, 5, 4, 5, 6, 7, 8, 9]
look = 5

print(find(ints, look))

strs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
look = 'h'

print(find(strs, look))

classes = [int, str, float, bool, list, dict, tuple, set, complex]
look = None

print(find(classes, look))

