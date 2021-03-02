class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, "-->", end=' ')
            current_node = current_node.next
