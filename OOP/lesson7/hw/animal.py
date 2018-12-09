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

class Animals:
  def __init__(self):
    self.name = ""
    self.weight = ""
    
  def eat(self):
    print("<p>",self.name, 'is eating now..', "</p>")
    
class Dogs(Animals):
  def speak(self):
    print("<audio src=woof.mp3 autoplay></audio>")
    
class Cats(Animals):
  def speak(self):
    print("<audio src=meow.mp3 autoplay></audio>")
    
class Fox(Animals):
  def speak(self):
    print("<audio src=blah.mp3 autoplay></audio>")
    
dog1 = Dogs()
dog1.name = "Shelby"
cat1 = Cats()
cat1.name = "Charlie"
foxy = Fox()
foxy.speak()

dog1.speak()
cat1.speak()
dog1.eat()
cat1.eat()