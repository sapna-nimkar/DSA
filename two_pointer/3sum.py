from typing import List, Dict

'''
3Sum : in an array, determine such 3 numbers whose sum is equal to a given target number
'''

def awesome_3sum(n: List[int], target: int) -> bool:
    unique = set(n)
    n.sort()
    i = 0
    j = len(n) -1
    while i < j:
        possible = n[i] + n [j]
        if possible > target:
            j -= 1
        elif possible == target:
            if 0 in unique:
                result = [n[i], n[j], 0]
                return True
        else:
            probable = target - possible
            if probable in unique:
                return True
            else:
                i += 1
    return False

print(awesome_3sum([3,1,8,5], 20))