# dictionary have setdeafult function(key,default value)
# if there is already key then don't set anything
d = {}
d.setdefault(1,1)
d.setdefault(1,2)
#print(d)

s = {}
node = 1
if node not in s:
    s[node] = set([3])

s[node].add(4)

print(type(s[node]))
#s[1].add(1)
s[node].remove(3)
s[node].remove(4)
if s[node]:
    print("yes")
print(s)

g = set([1])
print(bool(g))

s[1] = 3
s['2'] = [2]
s[3] = {2}
print(s)


# adj list
