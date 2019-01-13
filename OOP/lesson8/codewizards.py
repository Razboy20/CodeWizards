#!/usr/bin/python
print("Content-Type:text/html")
print()

import cgi,cgitb
cgitb.enable()

########### E X E R C I S E S ###########
#
# Exercise 1: Create the Programmer and Wizard classes.
#
# Exercise 2: Create a Codewizards class and inherit it from Programmer & Wizard.
#
# Exercise 3: Show the name of our codewizard.
#
# Exercise 4: Add wizard points to our wizard.
#
# HOMEWORK: Add skills to our Programmer class
# Step 1: Inside constructor, add new attribute skills
#
# Step 2: Create a new method setSkills with two parameters self & mySkills.
#
# Step 3: Inside setSkills, set the skills attribute to given mySkills parameter.
# 
# Set skills from the constructor of Codewizard class, and show them in showInfo method.
# This homework is quite similar to what we did in exercise 4 of today's class.
#
########################################
class Programmer: 
  def __init__(self, name): 
    self.name = "Programmer " + name

class Wizard: 
  def __init__(self, name): 
    self.name = "Wizard " + name
    self.wizardPoints = "0"
  def setWizardPoints (self, points):
    self.wizardPoints = points

class Codewizards(Wizard,Programmer): 
  def __init__(self, name, points): 
    super().__init__(name)
    self.setWizardPoints(points)
  def showlnfo(self): 
    print("<h1>" + self.name + "</h1>")
    print("<p>Wizard Points: " + self.wizardPoints + "</p>")
    
wizardl = Codewizards('Akhil', "OVER 9000")
wizardl. showlnfo() 


