#enqueue, deuqueany, dequeCat, dequedog

from collections import deque
class Shelter:
    def __init__(self):
        self.queue = deque([])

    def enqueue(self,animal):
        if animal == "cat" or animal == "dog":
            self.queue.append(animal)

    def dequeAny(self):
        return deque.popleft()

    def dequeCat(self):
        stack = []
        cat = ""
        queue = self.queue
        while(queue.peek() != "cat"):
            stack.append(queue.popleft())

        # check if we found cat
        if (len(queue) == 0):
            cat = None
            print("No Cats")
        else:
            cat = queue.popleft()

        # put everything on stack back to queue
        while(stack):
            queue.appendleft(stack.pop())

        return cat



