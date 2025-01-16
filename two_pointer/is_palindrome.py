
'''
determine a string s is a palindrome
'''

def is_palindrome(s: str) -> bool:
    for i in range(len(s)//2):
        j = len(s) - i -1
        if s[i] != s[j]:
            return False
    return True

print(is_palindrome('abbabba'))