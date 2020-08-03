'''

check http

what is 1 / or 2 //

or no http
'''


'''
1. host name is case insensitiev


http://abc.com:
hostname:port//

if you see %. Take next two char and try convert

1. func to hex to string
2. func check strings are same case insensitive


1. split both url ";"
1. split string by /
3. check if same size
4. check each section. 
4. 0 lower case both words
5. if 1 index hostname:por
6. check if rest of string the same
'''

'''
def hex_str(idx, string):
    str_hex = string[idx:idx + 2]
    return idx + 1, chr(int(str_hex, 16))


def equal_str(str1, str2):
    idx1, idx2 = 0, 0
    while idx1 < len(str1) and idx2 < len(str2):
        chr1, chr2 = str1[idx1], str2[idx2]
        # check if need to convert hex
        if chr1 == "%":
            idx1, chr1 = hex_str(idx1 + 1, str1)
        if chr2 == "%":
            idx2, chr2 = hex_str(idx2 + 1, str2)
        # check if char are equal
        if chr1.lower() != chr2.lower():
            print(chr1, chr2)
            return False
        # update index
        idx1 += 1
        idx2 += 1
    print(idx1, len(str1), str1, idx2, len(str2), str2)
    return idx1 == len(str1) and idx2 == len(str2)


def url_same(urls):
    urls = urls.split(";")

    # not two url
    if len(urls) != 2: return False

    # split url by /
    url1, url2 = urls
    url1, url2 = url1.split("/"), url2.split("/")
    # check len
    if len(url1) != len(url2): return False

    # check scheme case insensitive
    if not equal_str(url1[0], url2[0]): return False

    # check the hostname:port
    hp1 = url1[2].split(":")
    hp2 = url2[2].split(":")
    port1, port2 = "80", "80"
    if not equal_str(hp1[0], hp2[0]): return False

    if len(hp1) == 2: port1 = hp1[1]
    if len(hp2) == 2: port1 = hp2[1]

    if not equal_str(port1, port2): return False

    # check rest of URL.
    for i in range(3, len(url1)):
        if not equal_str(url1[i], url2[i]):
            print(i)
            return False
    return True



print(url_same("http://abc.com:80/~smith/home.html;http://ABC.com/%7Esmith/home.html"))


hp = "aasdf"
h = hp.split(":")
print(h)
'''



'''
negative,
zero, one, two, three, four, five, six, seven, eight, nine,
ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen,
twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety,
hundred,
thousand,
million

1. neg_flag
2.

600 + 30 + 8


one thousand

one thousand five hundred

three hundred million five hundred thirty one thousand

300 * 1,000,000

300 000 500

hundred is not used when thousand can be

var
res
prev val

1. add number to res
2.

1. find million - can only occur once
2. find thousand

1. break into three sections.
2. func to convert to actual number
3. mult number by million of thousand

multiplier
2 million, 1 thousand, end of string * 1
divide by thousand every time

1. go through string find million and thousand
 find number of million and thousand

2. set mult
'''
word_num = {
"negative" : -1,
"zero" : 0,
"one" : 1,
"two" : 2,
"three" : 3,
"four" : 4,
"five" : 5,
"six" : 6,
"seven" : 7,
"eight" : 8,
"nine" : 9,
"ten" : 10,
"eleven" : 11,
"twelve" : 12,
"thirteen" : 13,
"fourteen" : 14,
"fifteen" : 15,
"sixteen" : 16,
"seventeen" : 17,
"eighteen" : 18,
"nineteen" : 19,
"twenty" : 20,
"thirty" : 30,
"forty" : 40,
"fifty" : 50,
"sixty" : 60,
"seventy" : 70,
"eighty" : 80,
"ninety" : 90,
"hundred" : 100,
"thousand" : 1000,
"million" : 1000000
}

def convert_sec_to_num(li_num):
    if len(li_num) == 0: return 0
    res = 0
    mult = 1

    # determine if need to multiply res by million or thousand
    last_num = li_num[-1]
    if last_num == "million" or last_num == "thousand":
        mult = word_num[last_num]
        li_num.pop()

    # process number
    for str_num in range(len(li_num)):
        num = li_num[str_num]
        if num == "hundred":
            res *= 100
        else:
            res += word_num[num]
    return res * mult


def convert_str_num(str_num):
    # initial checks
    words = str_num.split(" ")
    bool_neg = -1 if words[0] == "negative" else 1
    ptr = 1 if words[0] == "negative" else 0

    # find million and thousand
    num_sec = []
    for i,word in enumerate(words):
        if word == "million" or word == "thousand":
            print(word)
            num_sec.append(words[ptr:i+1])
            ptr = i+1

    # add tenth section in
    num_sec.append(words[ptr:len(words)])

    # process every million, thousand tenth section
    res = 0
    for sec in num_sec:
        res += convert_sec_to_num(sec)

    return bool_neg * res




print(convert_str_num("fifteen"))


'''
str_num = "one million two thousand two"
str_num.split("million")

print(str_num.split("thousand"))
'''