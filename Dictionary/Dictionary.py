# dictionary have setdeafult function(key,default value)
# if there is already key then don't set anything
d = {}
d.setdefault(1,1)
d.setdefault(1,2)
print(d)