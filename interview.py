from typing import Dict, List, Set
#find the frequency of each element in an array


def element_freq(data : List[str]) -> Dict[str,int]:
    result = {}
    for item in data:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result


result = element_freq(['a', 'b', '1', '5', '1', 'a', 'a'])
print(result)

# if in above string is given and it cannot be converted into list

def str_freq(data : str) -> Dict[str,int]:
    result = {}
    for item in data:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result

result = str_freq('sapna is doing tod fod no. 1')
print(result)

# print the duplicate elements of an array

def find_duplicates(data: List[str]) -> Set[str]:
    reference = set()
    result = set()
    for item in data:
        if item not in reference:
            reference.add(item)
        else:
            result.add(item)
    return result

print(find_duplicates(['a','d','a','s','s','s','g','a']))



# print the array in reverse order

def reverse_list(data : List[str]) -> List[str]:
    result = []
    for i in range(len(data)-1, -1, -1):
        result.append(data[i])
    return result

print(reverse_list(['a','d','c','s']))

# print the largest element in the array

def largest_ele(data : List[int]) -> int:
    largest = 0
    for item in data:
        if item > largest:
            largest = item
    return largest

print(largest_ele([1,4,7,6,2,8,0]))


# print the smallest ele in the array
def smallest_ele(data : List[int]) -> int:
    smallest = float('inf')
    for item in data:
        if item < smallest:
            smallest = item
    return smallest

print(smallest_ele([1,4,7,6,2,8,0]))

# print sum of all items in the array

def sum_of_all(data : List[int]) -> int:
    result = 0

    for item in data:
        result += item
    return result

print(sum_of_all([1,2,3,6]))

# sort the array in ascending order

def sort_me(data : List[int]) -> List[int]:
    result = []
    while len(data) >0:
        smallest = smallest_ele(data)
        result.append(smallest)
        data.remove(smallest)
    return result

print(sort_me([1,4,7,6,2,8,0]))


# find the second-largest element in the array

def second_largest(data : List[int]) -> int:
    largest = largest_ele(data)
    data.remove(largest)
    result = largest_ele(data)
    return result

print(second_largest([1,4,7,6,2,8,0]))

#find second smallest

def second_smallest(data : List[int]) -> int:
    smallest = smallest_ele(data)
    data.remove(smallest)
    result = smallest_ele(data)
    return result

print(second_smallest([1,4,7,6,2,8,0]))

# remove white spaces in the string

def paas_aao(data: str) -> str:
    result = ''
    for item in data:
        if item != ' ':
            result += item
    return result

print(paas_aao('sapna is on fire today'))

# prove that string is immutable
print('--------------')

def im_immutable(data: str):
    try:
        data + 's'
        data.__add__('s')
    except Exception as e:
        return e
    return data

print(im_immutable('sapna'))

# count the number of words in a string

def count_words(data: str) -> int:
    spacifier = {' ', ', ','. '}
    count = 1
    for letter in data:
        if letter in spacifier:
            count += 1
    return count

print(count_words('sapna will succeed, as I said. Mark my words.'))



# whether a string is Palindrome

def is_Palindrome(data: str) -> bool:

    for i in range(len(data)//2):
        if data[i] != data[len(data)-1-i]:
            return False
    return True

print(is_Palindrome('bozobj'))



#reverse a string

def reverse_str(data: str) -> str:
    result = ''
    for i in range(len(data)-1, -1, -1):
        result += data[i]

    return result

print(reverse_str('sapna'))

# remove leading zeros

def remove_zeros(data: str) -> str:
    result = ''
    for item in data:
        if item != '0':
            result += item
    return result

print(remove_zeros('000345'))

# print first letter of each word in a string

def first_letter(data: str) -> str:
    pacifier = {' ', ', ', '. '}
    result = data[0]
    for i in range(len(data)):
        if data[i] in pacifier:
            result += data[i+1]
    return result
print(first_letter('sapna will succeed, as I said. Mark my words.'))



# in string s, find the length of the longest substring without repeating chars

def longest_substring(data: str) -> str:
    largest_substring = ''
    for i in range(len(data)):
        ref = set()
        substr = []
        for j in range(i, len(data)):
            if data[j] not in ref:
                ref.add(data[j])
                substr.append(data[j])
            else:
                break
        if len(substr) > len(largest_substring):
            largest_substring = "".join(substr)
    return largest_substring



print(longest_substring('abcdeahki'))



# encode decode LEETCODE premium problem

"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

e.g
Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

Hint:
Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
"""

class Solution():
    # encodes the list into a single string
    def encode(self, l: List[str] ) -> str:

        result = ""
        for item in l:
            result = result + str(len(item)) + "#" + item
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_length = len(s[i: j+1])
            i = j + 1
            j = i + word_length
            word = s[i: j]
            result.append(word)
            i = j
        return result


    '''
    Grokking coding interview- how to prep for coding interviews course on educative.io
    85 hours
    '''

    # TWO POINTERS











