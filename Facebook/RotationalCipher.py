# loop every charcter
#   if alpha


# how do we rotate?
'''
if letter> see if it went past



input: rotationfactor, input

0-9 -> if the number 10 then we get back.

10 mod 9 will give 1
20 mod 9 will give 1

mod number of letter to get the number to add.


what is subtract?


9 mod rot 1:

first add.-> if leftover moving then mod rotfactor and that's answer
can we combine to make one equation

input: 9 and rot: 2 include 0

string - use ascii value to find ordering
max_limi

if (let+ rf > max_limit): done
else: mod eqn

(rf%9) - 1

1. rot letters
2. rot numbers rf%9-1


key: get the number to rotate down to [0-9,0-25]

pretend we already have

en = (c - '0')%9 + '0'
'''
#if 9+3 = 12 - 9 = 3
#if 8 + 3 = 13 - 9 =

#if rotation factor is too large

#if you look you have a problem

print(0%9)


def rot_num(c,rf):
    # rotate
    rot = (ord(c) - ord('0')+rf) % 10 + ord('0')

    return rot

def rot_let(c,rf):
    en = ''
    if c.isupper():
        en = (ord(c) - ord('A')+rf) % 26 + ord('A')
    else:
        en = (ord(c) - ord('a')+rf) % 26 + ord('a')
    return en

def rotate(input,rotation_factor):
    res = []
    for i, c in enumerate(input):
        if c.isalpha():
            en = rot_let(c,rotation_factor)
        elif c.isnumeric():
            en = rot_num(c,rotation_factor)
        else:
            en = ord(c)
        res.append(chr(en))
    return "".join(res)

input = 'abcdZXYzxy-999.@'
rotation_factor = 200
print(rotate(input,rotation_factor))

print()
#nopqrstuvwxyzABCDEFGHIJKLM9012345678