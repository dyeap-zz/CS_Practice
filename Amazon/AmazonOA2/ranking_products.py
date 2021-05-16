# https://aonecode.com/interview-question/ranking-products

'''
need to figure out how to sort by name (string), relevance, rating (int)

use a heap for these cases?

for relevance and rating and do that

sortKey

0,1,2

1 and 2 are the same.


always pick

if same choose by which comes first in list

store three things

(what you want to sort by, index, product_name). Can we just use the sort function instead of heap for same functionality
'''

'''
import heapq
a = 'a'
b = 'b'
c = 'c'
li = [[a,2,0],[a,1,2],[b,3,3],[c,1,3]]
li.sort(reverse = True)
li.sort(key=lambda x: (x[0],-x[1]), reverse=True)


print(li)

1. create - three things. what you want to sort by

loop:
    sort_key,i,name

if ascending then you're good no changes

if descending
    reverse = False

    x1_sign = neg

productperrow * rownum = what you start picking on

li[n,n+productsperrow]

'''


def ranking_products(numOfProducts,products,sortKey,sortOrder,productsPerRow,rowNumber):
    res = []
    pro = []

    sort_col = sortKey
    for i in range(len(products)):
        first = products[i][sort_col]
        second = i
        third = products[i][0]
        pro.append([first,second,third])

    # perform sort
    index_sign = 1
    rev = not(sortOrder)
    if rev == True:
        index_sign = -1
    print(rev)
    pro.sort(key=lambda x: (x[0],index_sign*x[1]), reverse = rev)
    print(pro)
    s = productsPerRow * rowNumber
    res = pro[s:s+productsPerRow]
    return [row[2] for row in (res)]



numOfProducts = 5
products = [
    ["product1",10,5],
    ["product2",10,3],
["product3",17,4],
["product4",9,4],
["product5",1,5],
]
sortKey = 2
sortOrder = False
productsPerRow = 3
rowNumber = 0
print(ranking_products(numOfProducts,products,sortKey,sortOrder,productsPerRow,rowNumber))


sort_key,i,name. Need increasing of index in case of tie