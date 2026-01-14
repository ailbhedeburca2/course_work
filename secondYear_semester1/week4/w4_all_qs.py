#!/usr/bin/env python3

#1. Create a Queue class using the approach shown in class, and add the following functionalities to it:

#Reversing a Queue recursively.
#Find the minimum value in the queue recursively.

#2. Write a function using the queue data structure to generate a sequence of binary numbers from 1 to n. 

#Example:

#Given n=16 the binary sequence is: 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000

#3.  Create a Stack class using the approach described in class. A letter means push and an asterisk means pop in the sequence below.  Write a script to show the sequence of values returned by the pop operations when this sequence of operations is performed on an initially empty LIFO stack.

#'EAS*Y*QUE***ST***IO*N***' ➞ ['S', 'Y', 'E', 'U', 'Q', 'T', 'S', 'A', 'O', 'N', 'I', 'E']

#4. A letter means put and an asterisk means get in the following sequence. Write a script to show the sequence of values returned by the get operation when this sequence of operations is performed on an initially empty FIFO queue.

#'EAS*Y*QUE***ST***IO*N***' ➞ ['E', 'A', 'S', 'Y', 'Q', 'U', 'E', 'S', 'T', 'I', 'O', 'N']

#5. Write a script that reads a sequence of characters and prints them in reverse order. Use a stack.

#6. Create a function to evaluate the following postfix expression using Stack data structure.

#"1432^*+147--+" ➞ 41

#7. Create a double ended queue class using the approach described in class. A palindrome is a word that is spelt the same backwards and forwards, such as "Bob" or "Navan".  Create an algorithm that verifies if a given word is a palindrome using the double ended queue.

class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        return self.list.pop(0)

    def size(self):
        return len(self.list)

    def empty(self):
        return len(self.list) == 0

    def first(self):
        return self.list[0]

    def last(self):
        return self.list[-1]

####################
#Q1
    def rev(self):
        if self.empty():
            return
        curr = self.dequeue()
        self.rev()
        self.enqueue(curr)


    def findMin(self):
        if self.empty():
            return None

        x = self.dequeue()

        if self.empty():
            self.enqueue(x)
            return x

        m = self.findMin()

        self.enqueue(x)

        if x < m:
            return x
        return m

#####################
#Q2

n = 16
q = Queue()
for i in range(1, n + 1):
    q.enqueue(bin(i)[2:])

########################
#Q3

class Stack(object):

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def top(self):
        return self.list[-1]

    def empty(self):
        return len(self.list) == 0

s = Stack()
str = 'EAS*Y*QUE***ST***IO*N***'
new_str = ''

for i in str:
    if i == '*':
        new_str += s.pop()
    else:
        s.push(i)

print(new_str)

#########################
#Q4

q = Queue()
new_str = ''

for i in str:
    if i == '*':
        new_str += q.dequeue()
    else:
        q.enqueue(i)

print(new_str)

############################
#Q5

s = Stack()
str = 'EAS*Y*QUE***ST*IO*N***'
new_str = ''

for i in str:
    s.push(i)

while not s.empty():
    new_str += s.pop()

print(new_str)

############################
#Q6

s = Stack()

equ = "1432^*+147--+"

for i in equ:
    if i.isdigit():
        s.push(int(i))
    else:
        num1 = s.pop()
        num2 = s.pop()
        if i == '^':
            s.push(int(num2) ** int(num1))
        elif i == '+':
            s.push(int(num1) + int(num2))
        elif i == '-':
            s.push(int(num2) - int(num1))
        elif i == '*':
            s.push(int(num1) * int(num2))
        elif i == '/':
            s.push(int(num2) / int(num1))

answer = s.top()
print(answer)

##################
#7

q = Queue()
str = 'acecar'
a = 0

half_str = str[:len(str)//2]

for i in range(len(half_str)):
    if half_str[i].lower() != str[len(str) - 1 - i]:
        a = 1
        break

if a == 1:
    print('not palindrome')
else:
    print('palindrome')

