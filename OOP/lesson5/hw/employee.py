#!/usr/bin/python
print("Content-Type:text/html")
print()

import cgi,cgitb
cgitb.enable()

########### H O M E W O R K ###########
#
# This file is totally yours.
# Be creative while practicing inheritance
#
########################################

class Employee:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def age(self):
    return(self.age)

class Worker(Employee):
  def __init__(self, name, age, job):
    Employee.__init__(self, name, age)
    self.specialization = job

  def age(self):
    return(Employee.age)
  def specialization(self):
    return(self.specialization)


worker1 = Worker("John", "21", "Computer Science")
print(worker1.age(), worker1.specialization())
