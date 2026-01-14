#!/usr/bin/env python3

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

