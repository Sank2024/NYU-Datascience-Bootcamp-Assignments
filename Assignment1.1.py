
# Write a function count_vowels(word) that takes a word as an argument
#  and returns the number of vowels in the word


user_input = input ("Please enter a word: ")


def count_vowels(user_input):
    vowels = "aeiouAEIOU"
    
    count = 0

    for char in user_input:
        if char in vowels:
            count += 1

    return count

print (count_vowels(user_input))
