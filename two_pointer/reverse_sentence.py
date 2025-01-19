'''
Reverse Words in a String
Given a sentence, reverse the order of its words without affecting the order of letters within the given word.
Constraints:
The sentence contains English uppercase and lowercase letters, digits, and spaces.
The order of the letters within a word is not to be reversed.
'''

def reverse_sentence(s: str) -> str:
    rs = s[::-1] #reversed sentence
    result = []
    start = 0
    end = 0
    while end < len(s):
        if rs[start] == ' ':
            start += 1
            end = start
        elif end == len(s) - 1 and rs[end] != ' ':
            resultant = rs[start:end+1]
            result.append(resultant[::-1])
            end += 1
        elif rs[end] != ' ':
            end += 1
        elif rs[end] == ' ':
            resultant = rs[start:end]
            result.append(resultant[::-1])
            end += 1
            start = end


    result_str = ' '.join(result)
    return result_str

print(reverse_sentence('Hello There     World All'))




