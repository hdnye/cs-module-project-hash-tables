import random

# Read in all the words in one go
with open("applications\markov\input.txt", 'r') as f:
    words = f.read()

# split input into ind'l words
words = words.replace('\n', ' ')
text = words.split(' ')
print(text)
# TODO: analyze which words can follow other words
# Your code here
# begining code to set ht
text_ht = {}
for i in range(len(text)):
    # set loop to pass over empty strings
    if text[i] is "" or text[i + 1] is "":
        continue
    # add key:value to ht
    if text[i] not in text_ht:
        text_ht[text[i]].append(text[i + 1])
    # find next word
    else:
        text_ht[text[i]] = [text[i + 1]       


# TODO: construct 5 random sentences
# Your code here



    # """
    # Plan for implementation:    
    # - create ht to store k:v from txt file
    # - create __after__function to find the k:v pairs of words
    #     - for word in text if word != word - 1: ht[value] = key
    #     - elif word + 1 != word -1: ht[key] = value
    # - loop through .txt & add pairs to ht

    # After ht has its k:v pairs:
    # - set start/stop variables
    # - new f() to generate random sentences
    #     - random will need to be set to begin w 'start'
    #     - & end with 'stop'
    #     - will need to reconstruct the sentence structure from the split strings
    # """
