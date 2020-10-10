def no_dups(s):
    # Your code here
    # set() built-in f() only returns distinct elements
    # .split() method separates the words in the str
    my_list = set()
    words = s.split()
    result = ''

    for word in words: 
        if word not in my_list:
            my_list.add(word)
            result += word + ' '
    
    return result[:-1]

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
