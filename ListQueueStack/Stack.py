class Node():
    # constructor for a node with value
    def __init__(self,val):
        self.val = val;
        self.next = None;

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self,val):
        newNode = Node(val)
        if (self.length == 0):
            self.bottom = newNode
        else:
            # stack is not empty
            newNode.next = self.top
        self.top = newNode
        self.length += 1

    def pop(self):
        pop_node = self.top
        if (self.top == None):
            return None
        if (self.top == self.bottom):
            self.bottom = None

        self.top = self.top.next
        self.length -= 1
        return pop_node
        '''
        top_node = self.top
        node_before_top = self.bottom
        for _ in range(0,self.length - 2):
            node_before_top = node_before_top.next
        node_before_top.next = None
        self.top = node_before_top
        self.length -= 1
        return top_node.val
        '''

    def print(self):
        top = self.top
        while(top):
            print(top.val, end = "->")
            top = top.next
        print("None")
        print(f"length = {self.length}")

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(5)
stack.pop()
stack.pop()
print(f"Top = {stack.peek().val}")
stack.print()