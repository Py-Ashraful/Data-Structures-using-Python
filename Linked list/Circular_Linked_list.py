class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Circular_linked:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        new_node = Node(data)
        current_node = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node

        else:
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data + " --> ", end=" ")
            current_node = current_node.next
            if current_node == self.head:
                break


if __name__ == "__main__":
    cir = Circular_linked()
    cir.append("A")
    cir.append("D")
    cir.append("C")
    cir.insert_beg("F")
    cir.print_list()
