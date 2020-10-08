def word_count(s):
    # Your code here
    d = {}
  
    for words in s.split():
        words = words.strip(r": , . - + = / \ | [] {}() * ^ & ")
        words = words.lower()        
        if words in d:
            d[words] += 1
        else:
            d[words] = 1  
        return d        
   

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))



# letter_count example
# def letter_count(string):
#     # create an empty list
#     d = {}
#     # loop through string
#     for char in string: 
#         # is it in the string? increment its value
#         if char in d:
#             d[char] += 1
#         else:
#         # if it does not exist, add it to dict
#             d[char] = 1
#     return d  

# def print_sorted_letter_count(string):
#     # get the sorted dict
#     d = letter_count(string)    
#     # convert dict to a list
#     # built-in items()
#     items = list(d.items())
#     print(items)
#     # print the items out in alph order
#     # built-in function similar to ()=> in JS
#     # ex: items.map((item) => { console.log(item) })
#     items.sort(key=lambda item: item[0].lower(), reverse=False)
#     print(items)
#     # this will print the most used char's
#     for i in items:
#         print(f'{i[0]}: {i[1]}')

# if __name__ == "__main__":
#     print(letter_count(""))
#     print(letter_count("Hello"))
#     print(letter_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
#     print(print_sorted_letter_count(
#         'This is a test of the emergency broadcast network. This is only a test.'))
