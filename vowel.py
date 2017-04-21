#!/usr/bin/env python3
output = input('Input Sentence:')
print (output)
char_count = len(output)

print ("There are " + str(char_count) + " characters in your sentence.")

#vowel_count = 0

#def countvowels(output):
    
    #for char in ouput:
        #if char == "a" or "e" or "i" or "o" or "u":
            #vowel_count = vowel_count + 1
    #return vowel_count

#print ("There are " + str(vowel_count) + " vowels in your sentence.")
vowel_a = output.ignorecase.count('a')
vowel_e = output.count('e')
vowel_i = output.count('i')
vowel_o = output.count('o')
vowel_u = output.count('u')

print ("you used the letter A " + str(vowel_a) + " times")
print ("you used the letter E " + str(vowel_e) + " times")
print ("you used the letter I " + str(vowel_i) + " times")
print ("you used the letter O " + str(vowel_o) + " times")
print ("you used the letter U " + str(vowel_u) + " times")