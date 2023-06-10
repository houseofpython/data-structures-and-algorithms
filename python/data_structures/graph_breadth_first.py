from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_node(self, node):
        self.graph[node] = []
        
    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
        
    def breadth_first(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        result = []

        while queue:
            current_node = queue.popleft()
            result.append(current_node)

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return result

    def display_collection(self, collection):
        print(collection)
