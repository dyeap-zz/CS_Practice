class ListNode(object):
 def __init__(self, x):
     self.val = x
     self.next = None


head = ListNode(1)
ptr = head
ptr.next = ListNode(2)
ptr = ptr.next
ptr.next = ListNode(3)

ptr = head
while ptr:
    print(ptr.val)
    ptr = ptr.next

def increment(l1,li):
    print(l1,li)
    l1.next = 3
    li = 5
    #l1 = l1.next
    #li[0] = head.next
    return
li = [head]
increment(head,li)
print(head,head.next,li)

# class objects are mutable. Within another function the callee can change everything about it
# you can't modify the object itself by changing it to something else

def increment(head,li):
    # this change head.next to have Node 5
    head.next = ListNode(5)
    # but you can't change head itself. This won't change head on the way back
    head = head.next

    # this will change li
    li[0] = 1
    # this will not change li.
    li = [4]
