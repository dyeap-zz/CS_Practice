li = [0.1,1.1]
print(all(isinstance(item, float) for item in li))
print(all(type(item) == float for item in li))

li = [0.0,1.0]
# check if item in range
print(all(0<=item<=1 for item in li))

