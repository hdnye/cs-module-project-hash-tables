# Your code here
import collections

with open('applications/histo/robin.txt', 'r') as f:
    words = f.read()
    words, text = words.replace('\n', ' '), words.split()    
    
# first output: # of words   
    d = {}
    for word in text:
        word = word.strip('" : ; , . - + = / \\ | [ ] { } ( ) * ^ &')
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    print(d)

# second output: alphabetically    
    items = list(d.items())
    items.sort(key=lambda item: item[0].lower(), reverse=False)
    for i in items:
        print(f'{i[0]} : {i[1]}')
