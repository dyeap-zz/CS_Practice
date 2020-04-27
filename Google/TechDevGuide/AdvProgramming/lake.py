'''
# input
https://www.youtube.com/watch?v=HmBbcDiJapY
input = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
output = 15 (1,7,7)

# brute force:

1. find all lake and compute volume


var keep track of last height computed
1. compute all peaks
1. compute volume two pointers
    -if increase or equal compute
    - else keep going
    - get left to catch up by taking min of current and next
'''


d = [1,2,2]
print(d.index(max(d)))

def comp_vol(heights):

    left, right = 0, 1
    vol = 0

    while (right < len(heights)):
        if (heights[right] >= heights[left]):
            low = min(heights[right],heights[left])
            left += 1
            while(left < right):
                vol += heights[left] * low
                vol = low
                left += 1
        right += 1
    # left catch up


    return vol


# got stuck from the decreasing cases. not sure how to deal w/o peaks






#heights = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
#print(comp_vol(heights))
