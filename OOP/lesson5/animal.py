#!/usr/bin/python
print("Content-Type:text/html")
print()

import cgi,cgitb
cgitb.enable()

########### E X E R C I S E S ###########
#
# Exercise 1: Let's start with parent class Animals
#
# Exercise 2: Create a child class dog and inherit it from animal.
#
# Exercise 3: Similarly, create a child class Cats and inherit it from Animals.
#
# Exercise 4: Let's bring these classes into action.
#
# _________ H O M E W O R K _________
# In Dogs class, add fetchBall method.
# In Cats class, add playWithString method. Show a related image in both methods.
#
########################################

class Animal:
  def __init__(self):
    self.name = ""
    self.weight = ""
  def eat(self):
    print(self.name + "is eating now...")

class Dog(Animal):
  def bark(self):
    print("<audio src='woof.mp3' autoplay></audio>")

class Cat(Animal):
  def purr(self):
    print("<audio src='meow.mp3' autoplay></audio>")
