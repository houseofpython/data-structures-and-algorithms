import pytest
import Graph from graph_breadth_first


graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')

expected = ['A', 'B', 'C']
actual = graph.breadth_first('A')


graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')

graph.add_edge('A', 'B')
graph.add_edge('C', 'D')

expected = ['A', 'B']
actual = graph.breadth_first('A')

