import pytest
from trees.binary_tree import Node, BinaryTree, BinarySearchTree

def test_pre_order():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    assert tree.pre_order() == [1, 2, 4, 5, 3]

def test_in_order():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    assert tree.in_order() == [4, 2, 5, 1, 3]

def test_post_order():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    assert tree.post_order() == [4, 5, 2, 3, 1]

def test_add():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.add(2)
    bst.add(4)

    assert bst.in_order() == [2, 3, 4, 5, 7]

def test_contains_true():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(3)
    bst.add(7)

    assert bst.contains(5)
    assert bst.contains(3)
    assert bst.contains(7)

def test_contains_false():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(3)
    bst.add(7)

    assert not bst.contains(6)
    assert not bst.contains(8)
    assert not bst.contains(0)
