# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# first pass: find the char's with the max & min values
# create dict
# find the max diff btn any two char's & assign to each other
# add to dict

with open('ciphertext.txt', 'r') as f:
    words = f.read()
    # print(words)

englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
                     'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_letter_count(words):
    letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                    'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for letter in words:
        if letter in LETTERS:
            letter_count[letter] += 1
    return letter_count

# find zero index
def get_first_index(x):
    return x[0]

# return the letters by most used to least
def get_frequency(words):
    # get dict of each ltr & it's count
    letter_freq = get_letter_count(words)
    # create dict to count each ltr w that frequency
    letter_to_freq = {}
    for letter in LETTERS:
        if letter_freq[letter] not in letter_to_freq:
            letter_to_freq[letter_freq[letter]] = [letter]
        else:
            letter_to_freq[letter_freq[letter]].append(letter)
    # put each list of letters in reverser ETAOIN order & convert to str
    for freq in letter_to_freq:
        letter_to_freq[freq].sort(key=ETAOIN.find, reverse=True)
        letter_to_freq[freq]= ''.join(letter_to_freq[freq])
    # convert freq dict to list of tuples & sort
    pairs = list(letter_to_freq.items())
    pairs.sort(key=get_first_index, reverse=True)
    # extract sorted letters for final string
    freq_order = []
    for pair in pairs:
        freq_order.append(pair[1])
    return ''.join(freq_order)
print(get_frequency(words))

# implement 2 f()s Encrypt & Decrypt
# Build a table to hold the char's & assign their new value
# encode_table = {
#     'A' : 'H',
#     'B' : 'Z',
#     'C' : 'Y',
#     'D' : 'W',
#     'E' : 'O',
#     'F' : 'R',
#     'G' : 'J',
#     'H' : 'D',
#     'I' : 'P',
#     'J' : 'T',
#     'K' : 'I',
#     'L' : 'G',
#     'M' : 'L',
#     'N' : 'C',
#     'O' : 'E',
#     'P' : 'X',
#     'Q' : 'K',
#     'R' : 'U',
#     'S' : 'N',
#     'T' : 'F',
#     'U' : 'A',
#     'V' : 'M',
#     'W' : 'B',
#     'X' : 'Q',
#     'Y' : 'V',
#     'Z' : 'S',
#     ' ' : ' '
# }
# decode_table = {}

# # will use the encode table to build the decode table
# def build_decode_table(encode_table):
#     for k, v in encode_table.items():
#         decode_table[v] = k
#     return decode_table

# build_decode_table(encode_table)
# print(build_decode_table(encode_table))

# # Encrypt will take a nomral Eng str & jumble it using a Caesar Cypher
# # (substitution cypher)
# def encrypt(string): 
#     encrypted_string = ''
#     # loop through string
#     for char in string:
#         encrypted_string += encode_table[char]
#     return encrypted_string

# print(encrypt('HELLO WORLD'))

# # Decrypt reverses the process
# def decrypt(string):
#     encrypted_string = ''
#     # loop through string
#     for char in string:
#         encrypted_string += decode_table[char]
#     return encrypted_string

# encrypted_message = encrypt("HELLO WORLD")
# print(decrypt(encrypted_message))
