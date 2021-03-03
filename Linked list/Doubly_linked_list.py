class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly_linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def append_beg(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            new_node.prev = self.head

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, "-->", end=" ")
            current_node = current_node.next


if __name__ == "__main__":
    dl = Doubly_linked_list()
    dl.append("A")
    dl.append("B")
    dl.append_beg("C")
    dl.print_list()
