'''

Given a string word and an abbreviation abbr, return TRUE if the abbreviation matches the given string. Otherwise, return FALSE.
A certain word "calendar" can be abbreviated as follows:
"cal3ar" ("cal end ar" skipping three characters "end" from the word "calendar" still matches the provided abbreviation)
"c6r" ("c alenda r" skipping six characters "alenda" from the word "calendar" still matches the provided abbreviation)
'''
from itertools import count
from symbol import comp_if


def valid_abbr(word: str, abbr: str) -> bool:
    i = 0
    j = 0
    print(word, len(word), abbr)
    while i < len(abbr):
        if abbr[i].isdigit():
            if abbr[i].isdigit() == 0:   #for leading zero case
                return False
            num = 0
            while i < len(abbr) and abbr[i].isdigit():
                num = num*10 + int(abbr[i])
                i += 1
            j += num
        else:
            if j >= len(word) or word[j] != abbr[i]:
                return False
            i += 1
            j += 1
    return j == len(word) and i == len(abbr)

print(valid_abbr('calendar', 'cal3ar'))
print(valid_abbr('calendar', 'cale1dar'))
print(valid_abbr('aaaaaaaaaaaa', 'a010a'))
print(valid_abbr('aaaaaaaaaaab', 'a10b'))
print(valid_abbr('institutionalized', 'i15d'))
print(valid_abbr('calendar', 'cale0dar'))
