class AdjacentNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, vertex_nums):
        self.vertex_nums = vertex_nums
        self.graph = [None] * self.vertex_nums

    def add_adj(self, src, dest):
        # adding Adjacen Node to sourc
        node = AdjacentNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # adding source to destination
        node = AdjacentNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.vertex_nums):
            print(i, end="")
            current_node = self.graph[i]
            while current_node:
                print(f" --> {current_node.data}", end="")
                current_node = current_node.next
            print(" \n")


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_adj(0, 1)
    graph.add_adj(0, 4)
    graph.add_adj(1, 2)
    graph.add_adj(1, 3)
    graph.add_adj(1, 4)
    graph.add_adj(2, 3)
    graph.add_adj(3, 4)
    graph.print_graph()
