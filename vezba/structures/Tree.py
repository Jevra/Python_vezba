from ..interfaces import TreeInterface
from .NodeTree import NodeTree


class Tree(TreeInterface):

    def __init__(self):
        self.root = None

    def add_node(self, information):

        element = NodeTree(information)

        if self.root is None:
            self.root = element
        else:
            node = self.root
            while True:
                if element.information < node.information:
                    if node.left is None:
                        node.left = element
                        element.parent = node
                        break
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = element
                        element.parent = node
                        break
                    else:
                        node = node.right

    def pre_order(self, node):
        if node is not None:
            print(node.information)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.information)
            self.in_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.information)

    def remove_node(self, info):

        if self.root is None:
            return

        node = self.root

        while node is not None:
            if node.information == info:
                break
            elif info < node.information:
                node = node.left
            else:
                node = node.right

        if node is None:
            print("There is no node with " + str(info) + " information!")
            return

        # if node has no child nodes
        if node.right is None and node.left is None:
            if node.parent:
                if node.parent.left is node:
                    node.parent.left = None
                else:
                    node.parent.right = None
                del node
            else:
                self.root = None

        # if node has one child
        elif (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
            if node.left:
                n = node.left
            else:
                n = node.right

            # if it is not root node
            if node.parent:
                if node.parent.left is node:
                    node.parent.left = n
                    n.parent = node.parent
                else:
                    node.parent.right = n
                    n.parent = node.parent
                del node
            # if it is root node
            else:
                self.root.left = n.left
                self.root.right = n.right
                self.root.information = n.information

        # if node has 2 children
        else:
            par = node
            succ = node.right
            while succ.left:
                par = succ
                succ = succ.left
            node.information = succ.information
            if par.left == succ:
                if succ.right:
                    par.left = succ.right
                    succ.right.parent = par
            else:
                if succ.right:
                    par.right = succ.right
                    succ.right.par = par