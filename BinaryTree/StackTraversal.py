from BST import BinarySearchTree

'''

         3
     0       5
-1      1  4      7
'''


bst = BinarySearchTree()
bst.add_node(3)
bst.add_node(0)
bst.add_node(-1)
bst.add_node(1)
bst.add_node(5)
bst.add_node(7)
bst.add_node(4)


bst.print_inorder()
print()


'''

#don't pop every time
1. if root is none: print->pop
2. if root has left: append
3. if root is none: stack pop

print()
1. if root is none: pop and print, set root = popped right
2. else: append to stack and root = root.left

'''

print()
def stack_print_no_dmg(root):
    if root is None: return
    stack = []
    while(stack or root):
        if root is None:
            root = stack.pop()
            print(root.val)
            root = root.right
        else:
            stack.append(root)
            root = root.left

stack_print_no_dmg(bst.root)
print()
'''
        4
    1       3
2       6  7  9
         9
         10
stack = [4,3,1,4]
root = bst.root

1. what can stack be used for to solve this problem?

what to visit next stakc

[9,3,7,4,6,1,2]
use a dctionary

9right = none
10 right = none

11

9
    10
  9    11

recursion

[4,1,2]
add root

1. if left node -> append. root.left = None
2. elif right node -> append root.right = None
3. else print/pop
'''


# this causes destruction of tree
def stack_print(root):
    if root is None: return
    stack = []
    stack.append(root)

    while stack:
        root = stack[-1]

        if root.left:
            stack.append(root.left)
            root.left = None

        elif root.right:
            print(root.val)
            stack.pop()
            stack.append(root.right)
            root.right = None


        else:
            print(root.val)
            stack.pop()

print()
stack_print(bst.root)