#!/usr/bin/env python3

class Memories(object):

  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

  def remember(self, element):
    if element == 'name':
      return self.name
    elif element == 'age':
      return self.age
    elif element == 'salary':
      return self.salary
    else:
      return 'False'

if __name__ == "__main__":
  person1 = Memories(name="Tom", age=32, salary=50000)

  print(person1.remember("salary"))   # expected 50000
  print(person1.remember("email"))    # expected False
  print(person1.remember("pet"))
  print(person1.remember("age"))
