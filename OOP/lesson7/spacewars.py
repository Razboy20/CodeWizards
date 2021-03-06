#!/usr/bin/python
print("Content-Type:text/html")
print()

import cgi,cgitb
cgitb.enable()

########### E X E R C I S E S ###########
#
# Exercise 1: Create a class Missile with a private target attribute.
#
# Exercise 2: Create three missiles and set it's target to those evil ships.
#
# Exercise 3: Set the missile target while creating object.
#
# Exercise 4: Create a nuclear missile from existing missile.
#
# Exercise 5: Fix the target of missile.
#
########################################

class Missile:
  def __init__(self, target):
    self.__target = target
  def shoot(self):
    print("<p>Missile fired at '"+self.__target+"'!</p>")
    if(self.__class__.__name__ == "NuclearMissile"):
      print("<p>You killed "+self.__target+"</p>")

class NuclearMissile(Missile):
  def __init__(self, target):
    Missile.__init__(self, target)

m1 = NuclearMissile("target1")
m1.shoot()

m2 = Missile("target2")
m2.shoot()

m3 = Missile("target3")
m3.shoot()
