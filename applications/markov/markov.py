import random

# Read in all the words in one go
with open("applications\markov\input.txt", 'r') as f:
    words = f.read()
    # split input into ind'l words
    text = words.split()
    print(text)

# TODO: analyze which words can follow other words
# Your code here
# begining code to set ht
    text_ht = {}
    for words in enumerate(text):
        word = words[0]
        next_word = words[1]
        # add keys to ht
        if word not in text_ht:
            text_ht[next_word] = [word]
        # find prev word
        else:
            text_ht[next_word].append[word]
    
print(text_ht)

# TODO: construct 5 random sentences
# Your code here



"""
Plan for implementation:    
    - create ht to store k:v from txt file
    - create __after__function to find the k:v pairs of words
        - for word in text if word != word - 1: ht[value] = key
        - elif word + 1 != word -1: ht[key] = value
    - loop through .txt & add pairs to ht

After ht has its k:v pairs:
    - set start/stop variables
    - new f() to generate random sentences
        - random will need to be set to begin w 'start'
        - & end with 'stop'
        - will need to reconstruct the sentence structure from the split strings
"""
