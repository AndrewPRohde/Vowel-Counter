#!/usr/bin/env python3
output = input('Input Sentence:')
print (output)
char_count = output.count(output)
str(char_count)
print ("There are ") + char_count + (" characters in your sentence.")

def countvowels(output):
    vowel = 0
    for char in ouput:
        if char in "aeiouAEIOU":
            vowel = vowel + 1
    return vowel
vowel_count = vowel
str(vowel_count)

print ("There are ") + vowel_count + (" vowels in your sentence.")
