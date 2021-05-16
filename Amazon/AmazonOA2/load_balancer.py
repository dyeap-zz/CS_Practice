# https://leetcode.com/discuss/interview-question/976039/Amazon-or-OA-or-Load-balancer/792631


def load_balance(arr):
    if len(arr) < 5:
        return False

    l, r = 1, len(arr) - 2
    leftsum = arr[0]
    rightsum = arr[-1]

    total = sum(arr)
    while l < r - 1:
        print("l= %d, r= %d" % (l, r))
        print("left_sum=%d ,right_sum = %d" % (leftsum, rightsum))
        midsum = total - leftsum - rightsum - arr[l] - arr[r]
        if (leftsum == midsum and rightsum == midsum):
            return True
        elif (leftsum < rightsum):
            leftsum += arr[l]
            l += 1
        elif (rightsum < leftsum):
            rightsum += arr[r]
            r -= 1
        else:
            leftsum += arr[l]
            rightsum += arr[r]
            l += 1
            r -= 1
    return False