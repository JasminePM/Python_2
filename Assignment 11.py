class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        #Insert a new node with given value to the tree
        if not self.root:
            self.root = Node(value)
        else:
            self.insert_recursion(self.root, value)

    def insert_recursion(self, node, value):
        if value < node.value:
            if node.left:
                self.insert_recursion(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self.insert_recursion(node.right, value)
            else:
                node.right = Node(value)

    def search(self, value):
        return self.search_recursion(self.root, value)

    def search_recursion(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self.search_recursion(node.left, value)
        else:
            return self.search_recursion(node.right, value)

if __name__ == "__main__":

    tree = BinarySearchTree()

    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)
    tree.insert(12)
    tree.insert(18)

    print(tree.search(10))
    print(tree.search(5))
    print(tree.search(100))
    print(tree.search(50))
    print(tree.search(18))