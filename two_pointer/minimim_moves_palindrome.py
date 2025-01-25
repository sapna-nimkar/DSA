'''
Minimum Number of Moves to Make Palindrome
Given a string s, return the minimum number of moves required to transform s into a palindrome.
In each move, you can swap any two adjacent characters in s.

'''

def count_moves(s: str) -> int:
    s = list(s)
    moves = 0
    i = 0
    j = len(s) -1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        elif s[i] != s[j]:
            k = j
            while k >= i:
                if s[i] == s[k]:
                    while k < j:
                        s[k], s[k+1] = s[k+1], s[k]
                        moves += 1
                        k += 1
                k -= 1
            j -= 1
            i += 1
            if k == i:
                moves += len(s) // 2 - i
    return moves

def count_moves_two(txt: str) -> int:
    s = list(txt)
    i, j = 0, len(s) - 1
    moves = 0
    while i < j:
        if s[i] != s[j]:
            k = j
            while s[k] != s[i]:
                k -= 1
            if k == i:
                return moves + len(s)//2 - i

            while k != j:
                s[k], s[k+1] = s[k+1], s[j]
                moves += 1
                k += 1
        i += 1
        j -= 1
    return moves

print(count_moves_two('ntiin'))
print(count_moves_two('xcxoxoc'))





