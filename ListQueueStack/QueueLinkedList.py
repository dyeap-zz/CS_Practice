class Node():
    # constructor for a node with value
    def __init__(self,val):
        self.val = val;
        self.next = None;
#first is one left and last is on the right to get O(1) access
class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self,val):
        enNode = Node(val)
        if (self.length == 0):
            self.first = enNode
            self.last = enNode
        else:
            self.last.next = enNode
            self.last = enNode
        self.length += 1

    def dequeue(self):
        if (self.length == 0):
            return None
        pop_node = self.first
        if (self.length == 1):
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return pop_node

    def print(self):
        first = self.first
        while(first):
            print(first.val, end = "->")
            first = first.next
        print("None")
        print(f"length = {self.length}")

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print()

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.print()
