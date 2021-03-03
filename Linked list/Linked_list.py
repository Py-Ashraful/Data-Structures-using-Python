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

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def append_beg(self, data):
        new_node = Node(data)
        if self.head is Node:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # find len linked list iterative way
    def len_iterative(self):
        count = 0
        current_node = self.head
        if current_node is None:
            return 0
        else:
            while current_node:
                count += 1
                current_node = current_node.next
            return count

        # find len by recursive waw

    def get_len_re(self, node):
        if not node:  # not node = if node is node
            return 0
        else:
            return 1+self.get_len_re(node.next)

    def len_recursive(self):
        return self.get_len_re(self.head)

    def after_node(self, data, node):
        current_node = self.head
        while current_node is not None:
            if node == current_node.data:
                break
            else:
                current_node = current_node.next
        if current_node is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def before_node(self, data, node):
        if self.head.data == node:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            pev = self.head
            while pev is not Node:
                if pev.next.data == node:
                    break
                else:
                    pev = pev.next
            if pev is None:
                print("Node not found")
            else:
                new_node = Node(data)
                new_node.next = pev.next
                pev.next = new_node

    def delete(self, node):
        if self.head.data == node:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node is not None:
                if node == current_node.data:
                    break
                else:
                    last_af = current_node
                    current_node = current_node.next
            if last_af.next.next == None and last_af.next.data == node:
                last_af.next = None
            elif current_node is None:
                print("Node is not found")
            else:
                current_node.data = current_node.next.data
                current_node.next = current_node.next.next

    def revase_iter(self):
        pev = None
        current_node = self.head
        while current_node:
            nxt = current_node.next
            current_node.next = pev
            pev = current_node
            current_node = nxt
        self.head = pev


llist = LinkedList()
llist.append("Ashraful")
llist.append("Islam")
llist.append_beg("Md")
# # list_size =llist.size()
# llist.after_node(".",  "Md")
# llist.after_node("age",  "Islam")
# llist.before_node("Ashraful",  "Md")
# print(llist.len_iterative())
# print(llist.len_recursive())
# llist.delete("Ashraful")
# llist.delete("Ashraful")
# llist.revase_iter()
# llist.delete("Islam")
llist.printList()
# print(list_size)
