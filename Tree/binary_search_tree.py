class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left == None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right == None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)

    def printTree(self, traversal_method):
        if traversal_method == "Inorder":
            self._printTree(self.root)

    def _printTree(self, current_node):
        if current_node:
            self._printTree(current_node.left)
            print(current_node.data)
            self._printTree(current_node.right)


if __name__ == "__main__":

    bt = BinarySearchTree()
    bt.insert(51)
    bt.insert(40)
    bt.insert(333)
    bt.insert(24)
    bt.insert(45)
    bt.printTree("Inorder")
