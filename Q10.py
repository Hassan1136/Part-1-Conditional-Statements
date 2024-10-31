
# 10. Write a program to determine if a given character is a vowel or consonant.

input_character = input("Enter a character: ")
vowel = "aeiouAEIOU"

if input_character in vowel:
    print(input_character, "is a vowel.")
else:
    print(input_character, "is a consonant.")