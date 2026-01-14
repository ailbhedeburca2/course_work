#!/usr/bin/env python3

#Q2. A template for a Tree data structure is provided below, along with a corresponding test class. Your task is to complete the implementation
# so that all tests pass successfully. The implementation must support both binary trees and general trees, depending on the configuration
# specified at creation. The provided test methods contain all the information required to correctly implement the Tree class.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.parent = None
        #binary
        self.left = None
        self.right = None
        #normal
        self.children = []

class Tree:
    def __init__(self, is_binary=True):
        self.root = None
        self.is_binary = is_binary

    def set_root(self, val):
        if not self.root:
            self.root = TreeNode(val)

    def is_leaf(self, node):
        if self.is_binary:
            return not node.left and not node.right
        return len(node.children) == 0

    def children(self, node):
        if self.is_binary:
            out = []
            if node.left:
                out.append(node.left)
            if node.right:
                out.append(node.right)
            return out
        return node.children

    def add_child(self, parent, val):
        if self.is_binary:
            raise ValueError("use insert_left/insert_right for binary trees")
        child = TreeNode(val)
        child.parent = parent
        parent.children.append(child)

    def insert_left(self, parent, val):
        if not self.is_binary:
            raise ValueError("use add_child for general trees")
        if parent.left is not None:
            raise ValueError("left already set")
        child = TreeNode(val)
        parent.left = child
        child.parent = parent

    def insert_right(self, parent, val):
        if not self.is_binary:
            raise ValueError("use add_child for general trees")
        if parent.right is not None:
            raise ValueError("right already set")
        child = TreeNode(val)
        parent.right = child
        child.parent = parent

    def preorder(self):
        out = []

        def dfs(node):
            if node is None:
                return
            out.append(node.val)
            for c in self.children(node):
                dfs(c)

        dfs(self.root)
        return out

    def postorder(self):
        out = []

        def dfs(node):
            if node is None:
                return
            for c in self.children(node):
                dfs(c)
            out.append(node.val)

        dfs(self.root)
        return out

    def inorder(self):
        if not self.is_binary:
            raise ValueError("inorder is only defined for binary trees")
        out = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            out.append(node.val)
            dfs(node.right)

        dfs(self.root)
        return out
