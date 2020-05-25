from collections import OrderedDict

S = "abcbaba"

range_dict = OrderedDict()
for i,char in enumerate(S):
    if char not in range_dict:
        range_dict[char] = [i,i]
    else:
        ranges = range_dict[char]
        range_dict[char] = [ranges[0],i]
print(list(range_dict))
for key,val in range_dict.items():
    print(key,val)

document = "practice. makes perfect. you'll only get Perfect by practice."
S = document.split(" ")

#order = OrderedDict()
order = {}
for char in S:
    if char not in order:
        order[char] = 1
    else:
        order[char] += 1

for k,v in order.items():
    print(k,v)