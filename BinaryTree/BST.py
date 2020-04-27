



class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

'''
-1
         3
     0       5
-1      1  4      7
'''


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def add_node(self,val):
        if (self.root is None):
            self.root = Node(val)
        else:
            self.add_node_traverse(self.root,val)

    def add_node_traverse(self,root,val):
        # This method does extra work by doing reassignment on nodes
        if(root is None):
            return Node(val)
        # guarantee root node
        if (val < root.val):
            left_node = self.add_node_traverse(root.left,val)
            root.left = left_node
        elif (val >= root.val):
            right_node = self.add_node_traverse(root.right, val)
            root.right = right_node
        return root

    ''''
    if (val < root.val):
        if (root.left is None):
            root.left = Node(val)
        else:
            self.add_node_traverse(root.left,val)
    # do right cond
    else:
        if (root.right is None):
            root.right = Node(val)
        else:
            self.add_node_traverse(root.right,val)
    '''

    def print_inorder(self):
        if (self.root is not None):
            self.inorder(self.root)

    # print left, root, right
    # always printing the left node first. Then the parent node. Then right node
    def inorder(self,root):
        if (root.left):
            self.inorder(root.left)
        print(root.val)
        if (root.right):
            self.inorder(root.right)

    def print_preorder(self):
        if (self.root is not None):
            self.preorder(self.root)

    # print root, left, right
    def preorder(self,root):
        print(root.val)
        if (root.left):
            self.preorder(root.left)
        if (root.right):
            self.preorder(root.right)

    # left, right, root
    def print_postorder(self):
        if (self.root is not None):
            self.postorder(self.root)

    def postorder(self,root):
        if (root.left):
            self.postorder(root.left)
        if (root.right):
            self.postorder(root.right)
        print(root.val)

    def lookup(self,val):
        root = self.root
        while(root):
            if (val == root.val):
                return root
            elif (val < root.val):
                root = root.left
            else:
                root = root.right
        return None

    def remove_node_from_tree(self,root):
        if (root.right):
            parent = root
            root = root.right
            while(root.left):
                parent = root
                root = root.left
            rep_val = root.val
            parent.right = None
            return rep_val
        elif (root.left):
            parent = root
            root = root.left
            while(root.right):
                parent = root
                root = root.left
            rep_val = root.val
            parent.left = None
            return rep_val
        else:
            return None

    def remove_node(self,val):
        root = self.root
        if (root is None):
            return None

        parent = root
        while (root):
            if (root.val == val):
                replacement_val = self.remove_node_from_tree(root)
                if (replacement_val is None):
                    if (parent.left and parent.left.val == val):
                        parent.left = None
                        return
                    elif (parent.left and parent.right.val == val):
                        parent.right = None
                        return
                    else:
                        self.root = None
                        return
                else:
                    root.val = replacement_val
                    return
            elif (val < root.val):
                parent = root
                root = root.left
            else:
                parent = root
                root = root.right
        return None





bst = BinarySearchTree()
bst.add_node(3)
bst.add_node(0)
bst.add_node(-1)
bst.add_node(1)
bst.add_node(5)
bst.add_node(7)
bst.add_node(4)
bst.remove_node(0)
print(bst.lookup(1))

bst.print_postorder()
a = 1