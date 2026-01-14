#!/usr/bin/env python3

#Q1.  A template for a singly linked list is provided below, along with a test class designed to verify your implementation. Your task is to
# complete the singly linked list so that all the provided tests pass successfully. The test methods contain all the information you need to
# correctly implement each function.

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_start(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def insert_end(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            new_node = Node(val)
            curr.next = new_node
            new_node.next = None
        self.size += 1

    def insert_sorted(self, val):
        if self.head is None:
            self.head = Node(val)
        elif val < self.head.val:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next.next and curr.val < val:
                curr = curr.next
            new_node = Node(val)
            new_node.next = curr.next
            curr.next = new_node
        self.size += 1


    def remove_start(self):
        if self.head is None:
            raise IndexError('List is empty')
        else:
            self.head = self.head.next
            self.size -= 1

    def remove_end(self):
        if self.head is None:
            raise IndexError('List is empty')
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
            self.size -= 1


    def find(self, val):
        if self.head is None:
            raise IndexError('List is empty')
        else:
            count = 1
            curr = self.head
            while curr.next and curr.val != val:
                count += 1
                curr = curr.next
            if count == self.size:
                return None
            else:
                return curr.val



    def is_empty(self):
        return self.size == 0


    def __len__(self):
        return self.size


    def display(self):
        output = []
        if self.head is not None:
            current = self.head
            while current:
                output.append(str(current.val))
                current = current.next
            print('->'.join(output))
        else:
            return None


if __name__ == '__main__':

    ll = SinglyLinkedList()
    ll.insert_start(1)
    ll.insert_end(2)
    ll.insert_end(3)
    ll.display()
    #ll.insert_start(4)
    #ll.insert_end(4)
    ll.insert_sorted(2.5)
    ll.display()
    ll.insert_sorted(0)
    ll.display()
    ll.remove_start()
    ll.display()
    ll.remove_end()
    ll.display()
    print(len(ll))
