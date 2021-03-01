class CircularQueue():

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, item):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is full")

        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def deque(self):

        if (self.front == -1):
            print("Queue is empty")

        elif (self.front == self.rear):
            de_que = self.queue[self.front]
            self.fornt = -1
            self.rear = -1
            return de_que
        else:
            de_que = self.queue[self.fornt]
            self.fornt = (self.fornt + 1) % self.size
            return de_que

    def display(self):
        if (self.front == -1):
            print("Queue is empty")
        elif(self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])
        else:
            for i in range(self.front, self.size):
                print(self.queue[i])
            for i in range(0, self.rear + 1):
                print(self.queue[i])


if __name__ == "__main__":

    q = CircularQueue(3)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(11)

    q.display()
