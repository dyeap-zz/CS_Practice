import sys
'''
d = {1:1}
e = {}
e.update(d)
e[2] = 2
print(d)
print(e)

x = [1,2,3,4,5]
'''
x = [1,2,3,4,5]
print(set(map(lambda num: num* num,x)))

inven = [(1,1)]
for m,c in enumerate(inven):
    print(m,c)



x = 30
y = 14
z = 10

print(x%y//z)