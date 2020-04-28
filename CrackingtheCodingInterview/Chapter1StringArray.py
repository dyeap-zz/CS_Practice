'''
# cc 1.6

1 2
3 4

2 4
1 3

1 2 3
4 5 6
7 8 9

temp variable

1. store in temp
2. replace it in row
3. store back

in place
perform swaps instead


1. take leftmost row swap with rightmost



n = 3

for row in num_row:
    for col in num_col

row = 0
col = num_col
while ():
    swap(grid[0][col],grid[row][0]
    row -= 1
    col += 1



3 4 7
2
1


1. stop until max_row + 1
2. stop until max_row

3 6 9
2   8
1 4 7


1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

1. top left swap = (0,num_rows))
2. top bottom swap  = (1,num_rows)
3. top right swap = (1,num_rows -1)

2. recursion until n reaches 1


second method
swap
top left = (0,i),(len-outer,i)
top bot = (i,),len-i
top right = i,len-i

for 1-n+1

#quickly code

n = 2 one outer
n = 3 one outer
n = 4 2 oute
n = 5 3
def rotate_image(image,n):
    if n = 2: # do once
    for outer in range(n,2):
        grid[0][]

    return image
'''

# cc 1.7

'''
1. if you see a 0 all its row col is 0

1. ordering is important

1. find all 0s
2. set row and col to 0
3. go through each row and col and set to 0


for first row and col do not do this until the end


def zeroOut(grid):
    if len(grid) < 1: return grid

    # detect and store positions of 0
    for row in range(1, len(grid)):
        for col in range(1, len(grid[row])):
            if grid[row][col] == 0:
                grid[row][0], grid[0][col] = 0, 0
                break

    # go through col and row and set respective
    for index in range(1,len(grid)):
        if grid[index][0] == 0 or grid[0][index] == 0:
            # set entire row to 0
            for row in range(1,len(grid)):
                grid[row][index] = 0
            for col in range(1,len(grid[0])):
                grid[index][col] = 0

    # set the 0 position to 0
    if grid[0][0] == 0:
        for col in range(1, len(grid[0])):
            grid[0][col] = 0
        for row in range(1, len(grid)):
            grid[row][0] = 0

    return grid


grid = [[1,0,1,1],
        [1,1,1,1],
        [1,1,1,1]]
print(zeroOut(grid))
'''
# 1.8
'''
1. write issubstring

use dictionary

check is s1 is substring of s2

shorter word = dictionary{let:num_occ}
if dictionary is empty then return True

def is_substring(shorter,longer):
    if len(longer) < len(shorter): return False

    dict1 = {}
    for let in shorter:
        if let not in dict1:
            dict1[let] = 1
        else:
            dict1[let] += 1

    for let in longer:
        if let in dict1:
            dict1[let] -= 1

    for val in dict1.values():
        if val > 0:
            return False
    return True

shorter = "watr"
longer = "aterw"
print(is_substring(shorter,longer))


def is_rotation(reg,rot):
    if (not is_substring(reg,rot)): return False

    reg_ptr = 0
    for rot_ptr in range(1,len(rot)):
        if (reg[reg_ptr] != rot[rot_ptr]):
            # reset reg_ptr
            reg_ptr = 0
        else:
            reg_ptr += 1

    rot_ptr = 0
    while(reg_ptr<len(reg)):
        if (reg[reg_ptr] != rot[rot_ptr]):
            return False
        reg_ptr += 1
        rot_ptr += 1
    return True

print(is_rotation(shorter,longer))
'''
