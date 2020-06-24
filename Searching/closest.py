Given list of nums and a number find the closest number to it

abs(desired-num) < min

[1,5,8,9,10] number = 8

As soon as you find number look L/R and take the abs val

if index is 0: take right
if index is at end: take left

repeating

[1,8,8,8,10]

if left or right == num: must repeat for both dir

must do recursively

Try BFS with storing the steps

# https://leetcode.com/discuss/interview-experience/694893/microsoft-sde2-hyderabad-offer

