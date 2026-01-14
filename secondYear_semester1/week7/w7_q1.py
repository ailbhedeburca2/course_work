#!/usr/bin/env python3

class TreeNode(object):
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        left_key = self.left.key if self.left else None
        right_key = self.right.key if self.right else None
        parent_key = self.parent.key if self.parent else None
        return f"key: {self.key}, value: {self.value}, left: {left_key}, right: {right_key}, parent: {parent_key}"

class Tree(object):

    def __init__(self):
        self.root = None

    def upsert(self, key, value):
        node = TreeNode(key, value)
        if self.root is None:
            self.root = node
            node.parent = None
            return self.root

        curr = self.root
        while True:
            if node.key < curr.key:
                    if curr.left is None:
                        curr.left = node
                        node.parent = curr
                        return curr.left
                    curr = curr.left
            elif node.key > curr.key:
                if curr.right is None:
                    curr.right = node
                    node.parent = curr
                    return curr.right
                curr = curr.right
            else:
                curr.value = node.value
                return curr

    def is_bst(self):
        if self.root is None:
            return
        node = self.root
        curr = self.root
        if curr.left:
            curr = curr.left
            while curr:
                if node.key > curr.key:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr = curr.right
                else:
                    if curr.left:
                        curr = curr.right
                    else:
                        curr = curr.right

    def find(self, key, value):
        node = TreeNode(key, value)
        if self.root is None:
            return None
        curr = self.root
        while curr:
            if node.key == curr.key:
                return curr
            elif node.key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return

    def before(self, node):
        if self.root is None:
            return
        curr = node
        if curr.left:
            n = curr.left
            while n.right:
                n = n.right
            return n

        while curr.parent and curr.parent.left == curr:
            curr = curr.parent
        return curr.parent

    def inorder_iterative(self):
        out = []
        if not self.root:
            return
        curr = self.root
        while curr.right:
            curr = curr.right
        while curr:
            out.append((curr.key, curr.value))
            curr = self.before(curr)
        return out[::-1]

    def print_paths(self, node):
        parents = []
        curr = node
        while curr != self.root:
            parents.append(str(curr.key))
            curr = curr.parent
        parents.append(str(self.root.key))
        print('->'.join(parents))

        children = []
        curr = node
        if curr.left:
            while curr.left:
                curr = curr.left
                children.append(str(curr.key))
        if curr.right:
            while curr.right:
                curr = curr.right
                children.append(str(curr.key))
        return '->'.join(children)


tree = Tree()
tree.upsert(10, 'A')
tree.upsert(5, 'B')
tree.upsert(12, 'C')
tree.upsert(2, 'D')
tree.upsert(7, 'E')
tree.upsert(16, 'F')
tree.upsert(11, 'G')
tree.upsert(14, 'H')
tree.upsert(1, 'I')

node = tree.find(7, 'E')
print(tree.before(node))

print(tree.inorder_iterative())
print(tree.print_paths(node))
tree.is_bst()

