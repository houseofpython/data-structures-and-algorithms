import pytest
from graph import Graph, Vertex

def test_add_vertex():
    graph = Graph()
    vertex = Vertex("A")
    graph.add_vertex(vertex)
    assert vertex.value in graph.adjacency_list

def test_add_edge():
    graph = Graph()
    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    graph.add_vertex(vertex1)
    graph.add_vertex(vertex2)
    graph.add_edge(vertex1, vertex2)
    assert vertex2 in graph.adjacency_list[vertex1]
    assert vertex1 in graph.adjacency_list[vertex2]
