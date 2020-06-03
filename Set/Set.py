s = set()
s.add(2)

# how to access the 2.
print(next(iter(s)))
print(s)
print(s.pop()) # gives the 2 but also removes it
print(s)