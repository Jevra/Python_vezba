import unittest
from vezba.structures import Tree


class TreeTestCase(unittest.TestCase):

    def setUp(self):
        self.binaryTree = Tree()

    def test_insert(self):
        assert(self.binaryTree.root is None)
        self.binaryTree.add_node(8)
        assert(self.binaryTree.root.information == 8)
        self.binaryTree.add_node(3)
        assert(self.binaryTree.root.left.information == 3)
        self.binaryTree.add_node(10)
        assert(self.binaryTree.root.right.information == 10)
        self.binaryTree.add_node(1)
        assert(self.binaryTree.root.left.left.information == 1)
        self.binaryTree.add_node(6)
        assert(self.binaryTree.root.left.right.information == 6)
        self.binaryTree.add_node(4)
        assert(self.binaryTree.root.left.right.left.information == 4)
        self.binaryTree.add_node(7)
        assert(self.binaryTree.root.left.right.right.information == 7)
        self.binaryTree.add_node(14)
        assert(self.binaryTree.root.right.right.information == 14)
        self.binaryTree.add_node(13)
        assert(self.binaryTree.root.right.right.left.information == 13)

    def test_remove(self):
        self.binaryTree.pre_order(self.binaryTree.root)
        self.binaryTree.remove_node(3)
        assert(3 not in self.binaryTree.preorderList)

    def test_pre_order(self):
        list = [8, 3, 1, 6, 4, 7, 10, 14, 13]
        self.binaryTree.add_node(8)
        self.binaryTree.add_node(3)
        self.binaryTree.add_node(10)
        self.binaryTree.add_node(1)
        self.binaryTree.add_node(6)
        self.binaryTree.add_node(4)
        self.binaryTree.add_node(7)
        self.binaryTree.add_node(14)
        self.binaryTree.add_node(13)
        self.binaryTree.pre_order(self.binaryTree.root)
        self.assertEqual(list, self.binaryTree.preorderList)


unittest.main()