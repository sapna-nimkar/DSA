'''
Given a string num representing an integer, determine whether it is a strobogrammatic number. Return TRUE if the number is strobogrammatic or FALSE if it is not.

Note: A strobogrammatic number appears the same when rotated
180 degrees (viewed upside down). For example, “69” is strobogrammatic because it looks the same when flipped upside down, while “962” is not.
'''

def is_strobogrammatic(n: str) -> bool:
    strobes = { '0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    # if len(n)%2 != 0 and n[len(n)//2] not in strobes:
    #     return False
    for i in range((len(n) + 1)//2):
        j = len(n) - 1 - i
        if n[i] not in strobes:
            return False
        elif n[j] not in strobes:
            return False
        elif strobes[n[i]] != n[j]:
            return False
    return True

print(is_strobogrammatic('969'))
print(is_strobogrammatic('606'))
print(is_strobogrammatic('818'))
print(is_strobogrammatic('69'))
print(is_strobogrammatic('828'))
print(is_strobogrammatic('8968'))
print(is_strobogrammatic('6969'))
