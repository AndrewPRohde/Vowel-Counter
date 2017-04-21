#!/usr/bin/env python3
output = input('Input Sentence:')
print (output)
char_count = len(output)

print ("There are " + str(char_count) + " characters in your sentence.")
output = output.lower()

vowel_a = output.count('a')
vowel_e = output.count('e')
vowel_i = output.count('i')
vowel_o = output.count('o')
vowel_u = output.count('u')

print ("You used the letter A " + str(vowel_a) + " times, E " + str(vowel_e) + " times, I " + str(vowel_i) + " times, O " + str(vowel_o) + " times, and U " + str(vowel_u) + " times.")
