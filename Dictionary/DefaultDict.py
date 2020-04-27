# default dictionary is same as dict except you can put in default values
# https://guide.freecodecamp.org/python/defaultdict/
# if key does not exist then you add in the value

from collections import defaultdict

# Yet another random key
random_key = "random_key"

# list defaultdict
list_dict_ = defaultdict(list)

# set defaultdict
set_dict_ = defaultdict(set)

# integer defaultdict
int_dict_ = defaultdict(int)

list_dict_[random_key].append("Hello World!")
set_dict_[random_key].add("Hello World!")
int_dict_[random_key] += 1

list_dict_[random_key].append("Hello World")

# if key does not exist then add it in
int_dict_[2] = 3

print(list_dict_)
print(set_dict_)
print(int_dict_)