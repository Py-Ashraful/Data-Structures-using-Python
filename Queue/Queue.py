class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def get_queue(self):
        if not self.is_empty():
            return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    # return len of the Queue
    def __len__(self):
        return len(self.items)


if __name__ == '__main__':

    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    print(q.get_queue())
    print(q.dequeue())
    print(q.is_empty())
    print(q.peek())
    print(len(q))
