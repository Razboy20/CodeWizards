#!/usr/bin/python
print("Content-Type:text/html")
print()

import cgi,cgitb
cgitb.enable()

########### H O M E W O R K ###########
#  Write code for the Amphibians example we discussed today.
#
# Create a class AquaticAnimals
# Inside that class
#  Add an instance attribute swimImage
#  Create a method to show the image stored in attribute swimImage
#
# Similarly create a class TerrestrialAnimals
# Inside that class
#  Add an instance attribute walkImage
#  Create a method to show the image stored in attribute walkImage
#
# Create another class Amphibians and inherit it from both AquaticAnimals and TerrestrialAnimals
#
# Inside that class
#  Set the attribute walkImage and swimImage inside constructor of this class.
#  Call swim() method using object of this class
#  Call walk() method using object of this class
########################################

class AquaticAnimals:
  def __init__(self):
    self.swimImage = ""

  def swim(self):
    print("<p>I can swim!</p>")
    print("<img src=" + self.swimImage + ">")

class TerrestrialAnimals:
  def __init__(self):
    self.walkImage = ""

  def walk(self):
    print("<p>I can walk!</p>")
    print("<img src=" + self.walkImage + ">")

class Amphibians(AquaticAnimals,TerrestrialAnimals):
  def __init__(self, swimImage, walkImage):
    self.swimImage = swimImage;
    self.walkImage = walkImage;

turtle = Amphibians('swimming.gif', 'walking.gif')
turtle.swim()
turtle.walk()
