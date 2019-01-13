#!/usr/bin/python
print("Content-Type:text/html")
print()

import cgi,cgitb
cgitb.enable()

########### H O M E W O R K - I ###########
#
# Inside the Animals class constructor method (__init__)
#    1: Add a new parameter animalName, and set the name attribute to this parameter
#    2: Print the name of animal
#
# Send the name while creating objects of any class Dogs, Cats, Fox
#
########### H O M E W O R K - II ##########
#
# Create a constructor method inside the Dogs class with three parameters
#   - self
#   - name
#   - breed
#
# Inside that method, set the instance attribute breed to given parameter
#
# Call the constructor method of parent class Animals using super
# Don't forget to send the name attribute alongwith it.
#
########################################

class Animal:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def eat(self):
    self.weight = self.weight+10
    print(self.name + "is eating now... He is now "+self.weight+" pounds.")

  def info(self):
    print(self.name+" is a "+self.__class__.__name__+" who weighs "+self.weight+" pounds.")


class Dog(Animal):
  def __init__(self, name, weight):
    Animal.__init__(name, weight)

  def bark(self):
    print("<audio src='woof.mp3' autoplay></audio>")

class Cat(Animal):
  def __init__(self, name, weight):
    Animal.__init__(name, weight)

  def purr(self):
    print("<audio src='meow.mp3' autoplay></audio>")

dog1 = Dog("Woofy", 56)
cat1 = Cat("Kittens", 101)

dog1.eat()
cat1.purr()
