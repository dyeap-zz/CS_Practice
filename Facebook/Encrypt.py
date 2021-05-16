'''
encrypt(s,en_s)
# base case
no s -> done
# recursive case
mid = n//2

append s

encrpyt(s_left[0:mid],en_s)
encryp(s_right[mid+1:end],en_s)


time - O(n)
space - O(n/2)
'''

def encrypt(s,en_s):
    n = len(s)
    # base case
    if n == 0: return

    # recursive case
    if n % 2 == 0: m = len(s)//2-1
    else: m = len(s)//2

    en_s.append(s[m])
    encrypt(s[0:m],en_s)
    encrypt(s[m+1:],en_s)

s = 'facebook'
en_s = []
encrypt(s,en_s)
print("".join(en_s))