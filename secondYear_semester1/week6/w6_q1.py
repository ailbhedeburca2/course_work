#!/usr/bin/env python3

#------------------ Question 1 ------------------

#Please take the partial Binary Search Tree implementation above and implement the additional methods below. I have also provided a test script on Loop (bst_impl_test.py). If the test script runs without error, it will indicate that your code is implemented well.

#upsert()

#first()

#last()

#before()

#Find the position/node before the current position in_order. Use the minimum possible hops, i.e. don't do a full in order traversal of the tree where possible.

#after()

#Find the position/node after the current position in_order. Use the minimum possible hops, i.e. don't do a full in order traversal of the tree where possible.

#in_order_using_before()

#implement the in_order algorithm using the before() method.

#in_order_using_after()

#implement the in_order algorithm using the after() method.

#find(key)

#Find a node with a particular key.

#delete()

class Position():

    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.right = None
        self.left = None

    def __repr__(self):
        return f"({self.key}, {self.value})"

class BinarySearchTree():

    def __init__(self):
        self.root = None

    def upsert(self, key, value):
        if self.root is None:
            self.root = Position(key, value)
            return self.root
        node = Position(key, value)
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
            elif node.key == curr.key:
                curr.value = node.value
                return curr

    def first(self):
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr

    def last(self):
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr

    def before(self, node):
        if node.left:
            n = node.left
            while n.right:
                n = n.right
            return n
        curr = node
        while curr.parent and curr.parent.left == curr:
            curr = curr.parent
        return curr.parent

    def after(self, node):
        if node.right:
            n = node.right
            while n.left:
                n = n.left
            return n
        curr = node
        while curr.parent and curr.parent.right == curr:
            curr = curr.parent
        return curr.parent

    def in_order_using_before(self):
        out = []
        node = self.last()
        while node:
            out.append(node.key)
            node = self.before(node)
        return out[::-1]

    def in_order_using_after(self):
        out = []
        node = self.first()
        while node:
            out.append(node.key)
            node = self.after(node)
        return out

    def find(self, key):
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            elif key == curr.key:
                return curr
            else:
                return None


    def delete(self, node):
        if node is None:
            return

        if node.parent is None or node.right is None:
            child = node.left if node.left else node.right

            if node.parent is None:
                self.root = child
                if child:
                    child.parent = None
                return

            if node.parent.left == node:
                node.parent.left = child
            else:
                node.parent.right = child

            if child:
                child.parent = node.parent
            return
        else:
            pred = self.before(node)
            node.key, node.value = pred.key, pred.value
            self.delete(pred)


if __name__ == '__main__':

    tree = BinarySearchTree()

    tree.upsert(10, 'A')
    tree.upsert(5, 'B')
    tree.upsert(15, 'C')
    tree.upsert(2, 'Q')
    tree.upsert(7, 'F')
    tree.upsert(12, 'P')
    tree.upsert(20, 'L')

    print(tree.first())
    print(tree.last())
    print(tree.find(15))
    print(tree.find(20))
    print(tree.find(0))
    node = tree.find(20)
    print(tree.before(node))
    tree.delete(node)
    print(tree.find(20))
