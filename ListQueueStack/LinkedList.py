class Node():
    # constructor for a node with value
    def __init__(self,val):
        self.val = val;
        self.next = None;


class LinkedList():
    def __init__(self,val):
        self.head = Node(val)
        self.tail = self.head
        self.length = 1
    def append(self,val):
        self.tail.next = Node(val)
        self.length += 1
        self.tail = self.tail.next
    def prepend(self,val):
        newNode = Node(val)
        newNode.next = self.head
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
        prev_node.next = newNode
    def remove(self,index):
        if (index > self.length - 1):
            index = self.length - 1
        prev_node = self.head
        if(index == 0):
            temp_ptr = self.head.next
            self.head.next = None
            self.head = temp_ptr
            self.lengt -= 1
            return
        for i in range(0,index-1):
            prev_node = prev_node.next
        temp_ptr = prev_node.next.next
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

linkedList = LinkedList(10)
linkedList.append(5)
linkedList.append(16)
linkedList.prepend(0)
linkedList.insert(4,19)
linkedList.remove(6)
linkedList.print()

