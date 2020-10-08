# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# first pass: find the char's with the max & min values
# create dict
# find the max diff btn any two char's & assign to each other
# add to dict









# implement 2 f()s Encrypt & Decrypt
# Build a table to hold the char's & assign their new value
encode_table = {
    'A' : 'H',
    'B' : 'Z',
    'C' : 'Y',
    'D' : 'W',
    'E' : 'O',
    'F' : 'R',
    'G' : 'J',
    'H' : 'D',
    'I' : 'P',
    'J' : 'T',
    'K' : 'I',
    'L' : 'G',
    'M' : 'L',
    'N' : 'C',
    'O' : 'E',
    'P' : 'X',
    'Q' : 'K',
    'R' : 'U',
    'S' : 'N',
    'T' : 'F',
    'U' : 'A',
    'V' : 'M',
    'W' : 'B',
    'X' : 'Q',
    'Y' : 'V',
    'Z' : 'S',
    ' ' : ' '
}
decode_table = {}

# will use the encode table to build the decode table
def build_decode_table(encode_table):
    for k, v in encode_table.items():
        decode_table[v] = k
    return decode_table

build_decode_table(encode_table)
print(build_decode_table(encode_table))

# Encrypt will take a nomral Eng str & jumble it using a Caesar Cypher
# (substitution cypher)
def encrypt(string): 
    encrypted_string = ''
    # loop through string
    for char in string:
        encrypted_string += encode_table[char]
    return encrypted_string

print(encrypt('HELLO WORLD'))

# Decrypt reverses the process
def decrypt(string):
    encrypted_string = ''
    # loop through string
    for char in string:
        encrypted_string += decode_table[char]
    return encrypted_string

encrypted_message = encrypt("HELLO WORLD")
print(decrypt(encrypted_message))
