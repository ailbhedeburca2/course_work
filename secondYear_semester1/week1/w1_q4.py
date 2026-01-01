#!/usr/bin/env python3

#Q4. Write a class called Test to take care of exam papers with the
# following attributes:

#subject_name
#correct_answers
#pasing_mark
#Instantiate a few objects based on Test, such as:

#paper1 = Test('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
#paper2 = Test('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
#paper3 = Test('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

#At the end, write a class called Student with the following
# attributes and methods:
#Attributes: name
#Methods: take_test()which takes one of the defined test objects
# above and a list of answers from student. The method must check
# whether the student passed the given test or not.

class Test(object):

  def __init__(self, subject_name, correct_answers, pasing_mark):
    self.subject_name = subject_name
    self.correct_answers = correct_answers
    self.pasing_mark = pasing_mark

class Student(Test):

  def __init__(self, name):
    self.name = name

  def take_test(self, paper, users_answers):
    num_correct = 0
    for i in range(len(paper.correct_answers)):
      if paper.correct_answers[i] == users_answers[i]:
        num_correct += 1

    questions = len(paper.correct_answers)
    value = 100 / questions
    percentage = num_correct * value
    if percentage > int(paper.pasing_mark[:-1]):
      return f'Passed {percentage}'
    else:
      return f'Failed {percentage}'

if __name__ == '__main__':

  paper1 = Test('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
  paper2 = Test('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
  paper3 = Test('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')


  stu1 = Student('Ailbhe')

  print(stu1.take_test(paper2, ['1C', '2C', '3D', '4A']))

  print(paper1.subject_name)
  print(paper2.correct_answers)
  print(paper3.pasing_mark)
