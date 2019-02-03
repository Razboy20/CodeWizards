#!/usr/bin/python3.6
from abc import ABC, abstractmethod
from random import randint
import cgitb
print("Content-Type:text/html")
print()

cgitb.enable()


########### E X E R C I S E S ###########
#
# Exercise 5: Get a random army of players instead of just one player.
#
# Exercise 6: So, similarly get an opponent army to fight with.
#
# Exercise 7: Use random image for players and opponents.
#
# Exercise 8: Create a fight method that will decide the winner.
#
########################################


class Playground():
  def __init__(self, image):
    self.players = []
    self.opponents = []
    self.image = image
    print("<img src=", self.image, ">")
    self.__title = ""

  def addPlayer(self, player):
    self.players.append(player)

  def addOpponent(self, opponent):
    self.opponents.append(opponent)

  def getTitle(self):
    return self.title

  def setTitle(self, title):
    self.title = title

  def fight(self):
    print("Fighting..")
    totalPlayers = len(self.players)
    totalEnemies = len(self.opponents)
    if(totalPlayers > totalEnemies):
      print("You won!!")
    elif(totalPlayers < totalEnemies):
      print("You lose!")
    else:
      print("It's a draw, refresh to play again")

myGame = Playground('arena.png')
myGame.setTitle('VS game')
print('<h1>', myGame.getTitle(), '</h1>')

class Character(ABC):
  def __init__(self):
    self.image = "blank.jpg"

  def show(self):
    print("<img src=", self.image, ">")

  @abstractmethod
  def setImage(self):
    return

class Player(Character):
  def setImage(self):
    randomNum1 = randint(1, 6)
    self.image = "player"+ str(randomNum1) +".png"

class Opponent(Character):
  def setImage(self):
    randomNum2 = randint(1, 6)
    self.image = "enemy"+ str(randomNum2) +".png"

playersCount = randint(1, 10)

print("<p>Here are our players</p>")
for x in range(playersCount):
   myPlayer = Player()
   myPlayer.setImage()
   myGame.addPlayer(myPlayer)
   myGame.players[x].show()

opponentsCount = randint(1, 10)

print("<p>Here are our opponents</p>")
for y in range(opponentsCount):
   myEnemy = Opponent()
   myEnemy.setImage()
   myGame.addOpponent(myEnemy)
   myGame.opponents[y].show()

myGame.fight()
