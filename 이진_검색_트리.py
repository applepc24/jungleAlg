class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(node, val):
    if val < node.val:
        if node.left is None:
            node.left = Node(val)
        else:
            insert(node.left, val)
    else:
        if node.right is None:
            node.right = Node(val)
        else:
            insert(node.right, val)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)

preorder = []
for line in sys.stdin:
    if line.strip():
        preorder.append(int(line.strip()))

root = Node(preorder[0])
for val in preorder[1:]:
    insert(root, val)

postorder(root)

    

