from collections import deque

1. put root on queue

2. while queue:
    curr_node - queue.pop
    curr_lvl = queue[:]
    while currlvl
        curr_node.right = popped node
        pop queue
        if left:
            add to queue
        if right:
            add to queue
    currnode.right = null



def connect_level(root):
    if root is None: return

    q = deque(root)
    while q: # b,c
        c_lvl = q.copy() # A
        q = deque()
        dummy_node = newNode(None,-1)
        p_node = dummy_node
        while c_lvl: # A
            nn = c_lvl.popleft()
            p_node.right = nn
            if nn.left:
                q.append(nn.left)
                nn.left = None
            if nn.right:
                q.append(nn.right)
                nn.right = None
            p_node = nn
        p_node.right = None
        dummy_node.right = None


