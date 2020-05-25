from collections import Counter

S = "abcabcbabc"

count = Counter()

# this is equivalent to below
count = Counter(S)

# counter is used like a regular dictionary
for char in S:
    if char not in count:
        count[char] = 1
    else:
        count[char] += 1

# if key does not exist then 0 is returned instead of exception occurring
print(count['z'])

bucket = [[] for _ in range(3)]
bucket[0].append(0)
print(bucket)

bucket[]