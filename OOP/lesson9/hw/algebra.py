#!/usr/bin/python
print("Content-Type:text/html")
print()

import cgitb
cgitb.enable()

from abc import ABC, abstractmethod

########### H O M E W O R K ###########
# Create an abstract class Algebra
# Inside that class
#   1) Create a constructor method with three parameters (self, num1, num2)
#      Inside it, Set attributes num1 and num2 from method parameters
#   2) Add an abstract method with name execute
#
# Create child class add from this abstract class.
# Inside that class
#   Create method execute with one parameter self
#     Inside that method, return that sum of attribute num1 and num2
#
# Similarly create class for subtract, multiply and divide
#
# Create an object of each class, and run the execute method to show result.
########################################

class Algebra(ABC):
  def __init__(self, table):
    self.table = table

  @abstractmethod
  def execute():
    pass


class Average(Algebra):
  def __init__(self, table):
    super().__init__(table)

  def execute(self):
    _sum = 0
    for item in self.table:
      _sum+=item
    ouput = _sum/self.table.length
    return(output)

average = Average([5, 1, 10])
print(average.execute())
