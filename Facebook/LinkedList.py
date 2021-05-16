'''
Input:
N = 6
list = [1, 2, 8, 9, 12, 16]
Output:
[1, 8, 2, 9, 16, 12]


1. reverse original
2. create your own

1. if odd: add everything from stack and add odd
2. store in stack

while stack:
    keep popping and add

helper function
reverse linked list(head,tail)

Reverse the actual values in the node

ht = reverse(start of even,
    while curr.next is even:
        pointer swap


p ->1<-2<-3<-4->5
    he       ht c
'''
def reverse_even(he):
    curr = he.next
    prev = he
    while curr:
        if curr.val%2==0:
            temp = curr.next
            curr.next = prev
            prev.next = None
            # update prev and curr
            prev = curr
            curr = temp
        else: break

    return prev

def reverse(head):
    curr = head
    while curr:
        if (curr.next and curr.next.val%2 ==0):
            ht = reverse_even(curr.next)

    return head



->2<-4 6
     p
       h