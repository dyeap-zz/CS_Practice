'''
<25
If inst > 1 (ceil): reduce by 1/2

25<=util<=60 nothing

>60
If not(2*inst<2*10^8): double inst

wait for 10 if double or reduce
'''

import math

def finalInstances(instances, averageUtil):
    i = 0
    print(2 * (10 ** 8))
    while i < len(averageUtil):
        # case for reducing
        util = averageUtil[i]
        if util < 25 and instances > 1:
            print("REDUCE")
            instances = math.ceil(float(instances) / 2)
            i += 10
        # print("2*inst = %d"%(2*instances))
        if util > 60 and not (2 * instances > 2 * (10 ** 8)):
            print("DOUBLE")
            instances *= 2
            i += 10

        i += 1
        print("i= %d" % i)
        print("instances=%d" % instances)
    return instances