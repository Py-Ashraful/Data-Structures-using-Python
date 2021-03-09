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
            self._inorder(self.root)
        elif traversal_method == "preorder":
            self._preorder(self.root)
        elif traversal_method == "postorder":
            self._postorder(self.root)
        elif traversal_method == "levelorder":
            self._levelorder(self.root)

    def _inorder(self, current_node):
        if current_node:
            self._inorder(current_node.left)
            print(current_node.data)
            self._inorder(current_node.right)

    def _preorder(self, current_node):
        if current_node:
            print(current_node.data)
            self._preorder(current_node.left)
            self._preorder(current_node.right)

    def _postorder(self, current_node):
        if current_node:
            self._postorder(current_node.left)
            self._postorder(current_node.right)
            print(current_node.data)

    def _levelorder(self, current_node):
        if current_node is None:
            return

        queue = []
        queue.append(current_node)
        while len(queue) > 0:
            print(queue[0].data)
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def hight(self):
        return self._hight(self.root)

    def _hight(self, current_node):
        if current_node is None:
            return 0
        left_hight = self._hight(current_node.left)
        right_hight = self._hight(current_node.right)

        if left_hight > right_hight:
            return left_hight+1
        else:
            return right_hight + 1

    def size(self):
        return self._size(self.root)

    def _size(self, current_node):
        if current_node is None:
            return 0

        stack = []
        stack.append(current_node)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size = size + 1
                stack.append(node.left)

            if node.right:
                size = size + 1
                stack.append(node.right)
        return size


if __name__ == "__main__":

    bt = BinarySearchTree()
    bt.insert(41)
    bt.insert(20)
    bt.insert(65)
    bt.insert(11)
    bt.insert(29)
    bt.insert(50)
    bt.insert(91)
    bt.printTree("Inorder")
    print()
    bt.printTree("preorder")
    print()
    bt.printTree("postorder")
    print()
    bt.printTree("levelorder")
    print()
    print(bt.hight())
    print()
    print(bt.size())
