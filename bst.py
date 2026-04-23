# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert function
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:     
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

# Inorder traversal
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

#Pre Order
def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

#Post Order
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")

def min(root):
    while root.right:
        root=root.right
    return root
def delete(root,val):
    if root is None:
        return root
    if (root.data<val):
        root.right=delete(root.right,val)
    elif(root.data>val):
        root.left=delete(root.left,val)
    else:
        if root.right is None:
            return root.left
        elif root.left is None:
            return root.right
        temp=min_node(root.right)
        root.data=temp.data
        root.right=delete(root.right,temp.data)
# Main
root = None

values = [10, 5, 15, 2, 7, 20]

for v in values:
    root = insert(root, v)

print("Inorder traversal:")
inorder(root)