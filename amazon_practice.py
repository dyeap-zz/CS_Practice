import heapq

#OA1
def convert_word_dict(word):
    my_dict = {}
    low_word = word.lower()
    for char in low_word:
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1
    return my_dict

def top_k_words_reviews(reviews,keywords,k):
    kw_occ_dict = {}
    res = []
    for keyword in keywords:
        kw_dict = convert_word_dict(keyword)
        kw_occ_dict[keyword] = 0
        for review in reviews:
            for i in range(len(review) - len(keyword) + 1):
                curr_word = review[i:i+len(keyword)]
                curr_dict = convert_word_dict(curr_word)
                if (curr_dict == kw_dict):
                    kw_occ_dict[keyword] -= 1
                    break
    li_kw = []
    for kw,occ in kw_occ_dict.items():
        li_kw.append([occ,kw])
    heapq.heapify(li_kw)
    for _ in range(k):
        popped = heapq.heappop(li_kw)
        res.append(popped[1] )
    return res


k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

print(top_k_words_reviews(reviews,keywords,k))

test = []
test.append([1,"b"])
test.append([1,"c"])
test.append([1,"a"])
test.append([1,"z"])

heapq.heapify(test)
for _ in range(4):
    print(heapq.heappop(test))

#OA2
import copy
def update_grid(i,j,grid,num_zom):
    if not (i<0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 1):
        grid[i][j] = 1
        num_zom += 1
    return num_zom

def min_hr_infection(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    num_zom = 0
    min_hr = 0

    for i in range(num_rows):
        for j in range(num_cols):
            if (grid[i][j] == 1):
                num_zom += 1

    while (num_zom < num_rows*num_cols):
        prev_grid = copy.deepcopy(grid)
        for i in range(num_rows):
            for j in range(num_cols):
                if (prev_grid[i][j] == 1):
                    num_zom = update_grid(i-1,j,grid,num_zom)
                    num_zom = update_grid(i+1, j, grid, num_zom)
                    num_zom = update_grid(i,j-1, grid, num_zom)
                    num_zom = update_grid(i, j+1, grid, num_zom)

        min_hr += 1
    print(grid)
    return min_hr


grid = [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

print(min_hr_infection(grid))




products = ["mobile","mouse","moneypot","monitor","mousepad"]
products.sort()
print(products)

#LC 1268



