# https://aonecode.com/amazon-online-assessment-five-star-sellers
# https://leetcode.com/discuss/interview-question/1037522/amazon-oa-five-star-sellers

'''
need to increase percentage of one that gives you highest percentage

compute threshold sum

thressum = thres * num_product * 1/100

while csum < thressum:

    loop all ratios and compute change percentage

    add all curr ratios together
    keep track of max change

all added ratio -= max_curr_ratio # because that's what you want to remove
change the curr ratio but incrementing
add to currsum and see if it passes threshold
'''

def fiveStartReviews(productRatings, ratingsThreshold):
    ratings = productRatings
    n = len(productRatings)
    tsum = ratingsThreshold * n * 1.0/100.0
    csum = 0
    for i in range(len(productRatings)):
        csum += float(ratings[i][0])/ratings[i][1]
    res = 0
    print(productRatings)
    while csum < tsum:
        csum = 0
        max_c = 0
        max_i = -1
        for i in range(n):
            numer = ratings[i][0]
            denom = ratings[i][1]
            print("numer=%d,denom=%d"%(numer,denom))
            frac = float(numer) / denom
            c = (float(numer+1))/(denom+1) - (float(numer)/denom)
            print("frace=%d,c=%d"%(frac,c))
            csum += frac

            if (c > max_c):
                print("i=%d"%i)
                max_c = c
                max_i = i

        print("\n")
        print("max_i = %d" %max_i)
        # subtract old ratio
        csum -= float(ratings[max_i][0])/ratings[max_i][1]
        ratings[max_i][0] += 1
        ratings[max_i][1] += 1
        csum += float(ratings[max_i][0])/ratings[max_i][1]


        res += 1
        #break
    return res











sum = thres * numofprod 1/100

while csum < rsum:

    # find the largest sum
    max_rate = 0
    loop rating:
        c = rate+1/rate+1 - rate/rate
        cums += rate/rate
        if c >maxrate
            maxrate =c
            index

    #subtract old rate
    csum -= old_rate[index]
    increment new rate + 1
    cum += new rate

