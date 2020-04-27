import requests


def conver_hex_to_decimal(bigram):
    dec_bigram = 0
    temp = ""
    for char in bigram:
        ascii_char = ord(char)
        hex_char = hex(ascii_char)
        split_hex = hex_char.split("x")
        temp += split_hex[-1]
    dec_bigram = int(temp, 16)
    return dec_bigram

#URL = "https://pastebin.com/raw/V5XpP3s0"
#res = requests.get(URL)
#print(res.text)

#data = res.text
data = "do or do not"
print(type(data))

bigram_dict = {}
for i in range(len(data)-1):
    bigram = data[i:i+2]
    if (bigram in bigram_dict):
        bigram_dict[bigram] = bigram_dict[bigram] + 1
    else:
        bigram_dict[bigram] = 1

test_dict = {" s":3, "tr":2, "st":2, "s ":2, "ri":2, "ng":2, "is":2, "in":2, "th":1, "sa":1, "pl":1, "mp":1, "le":1, "hi":1, "g ":1, "e ":1, "am":1, "a ":1, " i":1, " a":1}
if (test_dict == bigram_dict):
    print("Bigram dict created properly")

utf_freq = {}
max_dec = 0
for bigram,freq in bigram_dict.items():
    dec_bigram = conver_hex_to_decimal(bigram)
    if (dec_bigram > max_dec):
        max_dec = dec_bigram
    utf_freq[dec_bigram] = freq

print(utf_freq)
print(max_dec)
'''
# This part is not working
sparse_vector = [0]*max_dec+1
for utf,freq in utf_freq.items():
    sparse_vector[utf] = freq

print(sparse_vector)
'''


'''
char = "t"
ascii_char = ord(char)
hex_char = hex(ascii_char)

val = hex_char.split("x")
print(val)
#print(ord("t"))
#print(hex(116))
#print(type(hex(116)))
#s = "7468"
#print(int(s,16))
'''