class Node():
    # constructor for a node with value
    def __init__(self,val):
        self.val = val
        self.next = None
        self.previous = None


class LinkedList():
    def __init__(self,val):
        self.head = Node(val)
        self.tail = self.head
        self.length = 1
    def append(self,val):
        newNode = Node(val)
        self.tail.next = newNode
        newNode.previous = self.tail
        self.length += 1
        self.tail = self.tail.next
    def prepend(self,val):
        newNode = Node(val)
        newNode.next = self.head
        self.head.previous = newNode
        self.head = newNode
        self.length += 1
    def insert(self,index,val):
        # need to use two pointers
        self.length += 1
        if (index == 0):
            self.prepend(val)
            return
        prev_node = self.head
        for i in range(0,index-1):
            prev_node = prev_node.next
        newNode = Node(val)
        newNode.next = prev_node.next
        prev_node.next.previous = newNode
        newNode.previous = prev_node
        prev_node.next = newNode

    def remove(self,index):
        if (index > self.length - 1):
            index = self.length - 1
        prev_node = self.head
        if(index == 0):
            temp_ptr = self.head.next
            self.head.next = None
            self.head = temp_ptr
            self.head.previous = None
            self.length -= 1
            return
        for i in range(0,index-1):
            prev_node = prev_node.next
        temp_ptr = prev_node.next.next
        temp_ptr.previous = prev_node
        prev_node.next = temp_ptr

        if (index == self.length - 1):
            self.tail = prev_node
        self.length -= 1

    def print(self):
        head = self.head
        while(head):
            print(head.val,end = "->")
            head = head.next
        print("None")
        print(f"length = {self.length}")

        tail = self.tail
        while (tail):
            print(tail.val, end="->")
            tail = tail.previous
        print("None")
        print(f"length = {self.length}")


linkedList = LinkedList(10)
linkedList.append(5)
linkedList.append(16)
linkedList.prepend(0)
linkedList.print()
linkedList.insert(2,19)
linkedList.print()
linkedList.remove(1)
linkedList.print()


