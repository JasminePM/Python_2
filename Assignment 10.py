class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self.insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self.insert_recursive(current.right, value)

    def in_order(self):
        result = []
        self.in_order_recursive(self.root, result)
        return result

    def in_order_recursive(self, node, result):
        if node:
            self.in_order_recursive(node.left, result)
            result.append(node.value)
            self.in_order_recursive(node.right, result)

    def pre_order(self):
        result = []
        self.preorder_recursive(self.root, result)
        return result

    def preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self.preorder_recursive(node.left, result)
            self.preorder_recursive(node.right, result)

    def post_order(self):
        result = []
        self.postorder_recursive(self.root, result)
        return result

    def postorder_recursive(self, node, result):
        if node:
            self.postorder_recursive(node.left, result)
            self.postorder_recursive(node.right, result)
            result.append(node.value)


def test_bt():
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    bt.insert(2)
    bt.insert(7)
    bt.insert(12)

    print("in order traversal:", bt.in_order())
    print("pre-order traversal:", bt.pre_order())
    print("post.order traversal:", bt.post_order())

test_bt()
