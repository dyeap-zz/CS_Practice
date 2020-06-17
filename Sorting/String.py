def compare(n1, n2):
    return str(n1) + str(n2) > str(n2) + str(n1)

#print(compare(3,33))

# how does string comparator work?

print("3"<"4")
print("3"<"49")
print("3"<"30")
print("3000"<"31")

# string comparison checks leading digits first
# whichever digit is larger is considered the larger number overall
# so 300 < 4. 4 is considered larger
# when the digits are the same, it'll go to next digit and do the comparison again
# so 300 < 31 31 is considered larger

# checks the leading digit