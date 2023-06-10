import pytest
from graph import Graph

@pytest.fixture
def graph():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')

    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')

    return g

def test_depth_first(graph):
    start_node = 'A'
    expected = ['A', 'B', 'D', 'C']
    actual = graph.depth_first(start_node)
    assert actual == expected

pytest.main()
