# Write a function that returns the number (i.e., count) of vowels in a given string.
            # define function
            # determine if the character is a vowel or not
            # store the character -dict  
            # print dict 

# For this exercise, consider the following as vowels: a, e, i, o, u. The letter 'y' is not considered a vowel.

# Constraints:

# The input string will only consist of lowercase letters and/or spaces.

# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function

input=("here is a sentence to use")

def vowel_cont(input):
    numb_vowels = 0
    for v in input:
        if v in "aeiou":
            numb_vowels += 1;
        return numb_vowels
print(vowel_cont(input))
    

#Dylan's alternates

def vowel_count(astring):
    vowels = ({'a','e','i','o','u'})

print(vowel_count('aeioudddzzz'),5)



