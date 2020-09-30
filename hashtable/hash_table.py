# Class Notes
# O(1) time complexity
# Hash functions turn strings into numbers & must be deterministic

# hash() will return each ind'l character
# def hash_fn(s):
#     for char in s:
#         print(char)


# hash_fn('banana')

# encode() to return str ASCII number
# def hash_fn(s):
#     encoded_string = s.encode()
#     for byte_char in encoded_string:
#         print(byte_char)


# hash_fn('banana')

# get the sum of the ASCII in order to get the str's whole number
# not a good hash() algorithm to use in real life apparently
def hash_fun(s): #O(n) where n is length of string
    print(s)
    encoded_string = s.encode() #O(1)
    result = 0
    for byte_char in encoded_string:
        result += byte_char
    return result

print(hash_fun('banana'))
print(hash_fun('apple'))
print(hash_fun('paple'))

# map the results of hash() to an index in some array
# point is to quickly in O(1) TC to get to the data
# have to specify length of hash table
# modulo will bind the # from hash_fun to 0 by the len(array)
hash_array = [None] * 8

# store banana inside hash_array
hash_value = hash_fun('banana')
index = hash_value % len(hash_array)
# print(index)
# add/store value for key
hash_array[index] = ("banana","is yellow")
# print(hash_array)

# look up banana in hash_array
# get index value for banana
# can store k:v in a tuple
hash_value = hash_fun('banana') #O(n) but n === length of the string not the array
index = hash_value % len(hash_array)

print(hash_array[index])

# hash() + [] = hash_table

# to insert a k:v into hash_table
# - hash the key to convert it to a #
# - take the $ & % it by the size of the hash_table
# - insert the value into the index given by the % operation

# to retrieve a value given a specific key from a hash_table
# - hash the key to convert to a #
# - Use % to find index w/in underlying array
# - use this new index to find the value
hash_value = hash_fun('apple')
index = hash_value % len(hash_array) # convert the # into a new # btn 0 & len(arr)
print(hash_array[index])

print(hash_fun('eggg'))