class Adjnode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.n_node = vertices
        self.graph = [None]*self.n_node
