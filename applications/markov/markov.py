import random
from collections import defaultdict, Counter

# Read in all the words in one go
with open("applications\markov\input.txt", 'r') as f:
    words = f.read()

    # remove & replace any line breaks in the text files
    # split input into ind'l words
    words, text = words.replace('\n', ' '), words.split()
    text = [word for word in text if word != '']
    # print(text)

'''
example using the Markovify chain generator
text_model = markovify.Text(words)
# print(text_model)

# for i in range(5):
#     print(text_model.make_sentence())

# for i in range(3):
#     print(text_model.make_short_sentence(280))
'''
# TODO: analyze which words can follow other words
# Your code here
# begining code to set ht
dist_words = list(set(text))
word_index_dict = {word: i for i, word in enumerate(dist_words)}

k = 3

sets_of_k = [' '.join(text[i:i+k]) for i, _ in enumerate(text[:-k])]
print(sets_of_k)

# TODO: construct 5 random sentences
# Your code here

start = '"'
stop = '.?!"'
sentence = ''


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
