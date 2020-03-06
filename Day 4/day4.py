#Advent of Code 2015 Day 4
#written by Jacob Farabee

import hashlib

input = "yzbqklnj"
increment = 1
encode_string = ""
sentinel = False

while not sentinel:
    encode_string = input + str(increment)
    #encode input string and then hash in md5
    hash_bytes = hashlib.md5(encode_string.encode())
    #below: check whether hex (i.e. not byte) representation of MD5 hash has
    #first 5 characters as '00000'
    hash_string = hash_bytes.hexdigest()
    if hash_string[0:5] == "00000":
        print('Increment for five zeroes is ', increment)
    #part two of day 4 specifies a substring of 6 zeroes
    if hash_string[0:6] == "000000":
        print('Increment for six zeroes is ', increment)
        sentinel = True
    increment += 1
