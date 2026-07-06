class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        self.update_height(root)
        balance = self.balance_factor(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        self.update_height(root)
        balance = self.balance_factor(root)

        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.rotate_right(root)

        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.rotate_left(root)

        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def inorder(self, root, result=None):
        if result is None:
            result = []
        if root:
            self.inorder(root.left, result)
            result.append(root.key)
            self.inorder(root.right, result)
        return result

    def preorder(self, root, result=None):
        if result is None:
            result = []
        if root:
            result.append(root.key)
            self.preorder(root.left, result)
            self.preorder(root.right, result)
        return result

    def search(self, root, key):
        if not root:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)


if __name__ == "__main__":
    tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25]

    for v in values:
        tree.insert_key(v)

    print("Inorder:", tree.inorder(tree.root))
    print("Preorder:", tree.preorder(tree.root))

    tree.delete_key(40)
    print("After deleting 40:")
    print("Inorder:", tree.inorder(tree.root))

    print("Search 25:", tree.search(tree.root, 25))
    print("Search 100:", tree.search(tree.root, 100))
