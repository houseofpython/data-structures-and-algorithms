class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def get_node(self, vertex):
        if vertex in self.adjacency_list:
            return vertex
        else:
            return None

    def get_neighbor(self, vertex):
        return self.adjacency_list[vertex]

    def size(self):
        return len(self.adjacency_list)


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight
