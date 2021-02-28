class CircularQueue():

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, item):
        if ((self.rear + 1) % self.size == self.fornt):
            print("Queue is full")

        elif (self.front == -1):
            self.fornt = 0
            self.rear = 0
            self.queue[self.rear] = item

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
