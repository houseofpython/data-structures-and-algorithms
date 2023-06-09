import pytest
import unique_values_in_trees from tree_intersection

def test_unique_values_in_trees():
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    tree1 = Node(1)
    tree1.left = Node(2)
    tree1.right = Node(3)

    tree2 = Node(3)
    tree2.left = Node(4)
    tree2.right = Node(5)

    hashtable = Hashtable()

    expected = {1, 2, 3, 4, 5}
    actual = hashtable.unique_values_in_trees(tree1, tree2)

    assert expected == actual


def test_unique_values_in_trees_empty_trees():
    tree1 = None
    tree2 = None

    hashtable = Hashtable()

    expected = set()
    actual = hashtable.unique_values_in_trees(tree1, tree2)

    assert expected == actual
