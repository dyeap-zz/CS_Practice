class Stack():
    def __init__(self):
        self.length = 0
        self.list_val = []

    def peek(self):
        return self.top

    def push(self,val):
        self.list_val.append(val)
        self.length += 1

    def pop(self):
        if (self.length == 0):
            return None
        self.length -= 1
        pop_val = self.list_val.pop()
        return pop_val

    def print(self):
        for val in self.list_val:
            print(val,end = " ")
        print(f"length = {self.length}")

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(5)
stack.pop()

stack.print()


#print(f"Top = {stack.peek().val}")
