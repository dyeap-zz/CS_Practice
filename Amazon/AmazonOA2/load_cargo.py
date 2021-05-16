# https://aonecode.com/interview-question/load_cargo

'''
1. use max heapq -> make sure to multiple by -1
2. check that heapq looks good after you implement
3. use a double while loop to perform moving onto cargo


'''

import heapq


def loadTheCargo(num: int, containers: List[int], itemSize: int, itemsPerContainer: List[int], cargoSize: int) -> int:
    h = []
    res = 0
    for i in range(num):
        h.append([-itemsPerContainer[i], containers[i]])

    heapq.heapify(h)
    cargo = 0
    while h:
        num_items, num_containers = heapq.heappop(h)
        while cargo < cargoSize and num_containers > 0:
            res += -num_items
            num_containers -= 1
            cargo += 1
        if cargo == cargoSize: break
    return res
























