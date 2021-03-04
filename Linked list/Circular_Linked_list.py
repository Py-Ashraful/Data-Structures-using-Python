class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Circular_linked:
    def __init__(self):
        self.head = None

    def push(self, data):
        pass

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def print_list(self):
        pass
