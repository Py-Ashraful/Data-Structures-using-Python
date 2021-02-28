class Deque():
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []

    def removeFront(self):
        if not self.is_empty():
            return self.items.pop(0)

    def removeRear(self):
        if not self.is_empty():
            return self.items.pop()

    def frontPeek(self):
        if not self.is_empty():
            return self.items[0]

    def rearPeek(self):
        if not self.is_empty():
            return self.items[-1]

    def __len__(self):
        return len(self.items)

    def get_deque(self):
        return self.items


d = Deque()

d.addFront('A')
d.addFront('b')
d.addRear("C")

print(d.get_deque())

# print(d.removeFront())
# print(d.removeRear())
print(d.get_deque())
print(d.frontPeek())
print(d.rearPeek())

print(len(d))
