"""
Sort Colors
Given an array, colors, which contains a combination of the following three elements:
0(representing red)
1(representing white)
2 (representing blue)
Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue. Do not utilize the built-in sort function.
"""
from typing import List

def dutch_flag(a: List[int]) -> List[int]:
    start = 0
    current = 0
    end = len(a) -1

    while current <= end:
        if a[current] == 0:
            a[start], a[current] = a[current], a[start]
            start += 1
            current += 1
        elif a[current] == 1:
            current += 1
        else:
            a[current], a[end] = a[end], a[current]
            end -= 1
    return a

test = dutch_flag([1,0,1,2,2,1,1,0])
print(test)