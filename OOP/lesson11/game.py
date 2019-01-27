#!/usr/bin/python3.6
print("Content-Type:text/html")
print()

import cgitb
cgitb.enable()

from abc import ABC, abstractmethod

########### E X E R C I S E S ###########
#
# Exercise 1: Let's start with creating a class for our game.
#
# Exercise 2: Create an abstract class for characters in our game.
#
# Exercise 3: Create players and opponents from our abstract class Character.
#
# Exercise 4: Add player and opponent in our game.
#
########################################
# HOMEWORK: Add a private attribute title of our game, use get/set methods to save it's value.
#
# Step 1: Inside class Playground, add a private attribute title
# Step 2: Inside class Playground, add a method to set this title attribute.
# Step 3: Inside class Playground, add a method to get this title attribute.
# Step 4: Print the value of title using h1 tags.
########################################
# HOMEWORK 2: Save the game cover image in a attribute and use that.
#
# Step 1: Inside class Playground, add a parameter to constructor image
# Step 2: Save the image parameter as an attribute
# Step 3: In img tag, use the value from this attribute instead.
########################################

class Playground():
  def __init__(self):
    self.players = []
    self.opponents = []
    print("<img src='arena.png'>")

  def addPlayer(self, player):
    self.players.append(player)
  def addOpponent(self, opponent):
    self.opponents.append(opponent)

myGame = Playground()

#######

class Character(ABC):
  def __init__(self):
    self.image = "blank.jpg"

  def show(self):
    print(f"<img src={self.image}>")

  @abstractmethod
  def setImage(self):
    pass

#####

class Player(Character):
  def setImage(self, player):
    self.image = f"{player}.png"

class Opponent(Character):
  def setImage(self, enemy):
    self.image = f"{enemy}.png"

hero = Player()
hero.setImage("player6")
myGame.addPlayer(hero)
myGame.players[0].show()

monster = Opponent()
monster.setImage("enemy4")
myGame.addOpponent(monster)
myGame.opponents[0].show()
