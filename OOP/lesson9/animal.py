#!/usr/bin/python3.5
print("Content-Type:text/html")
print()

import cgitb, asyncio
cgitb.enable()
from abc import ABC, abstractmethod

########### E X E R C I S E S ###########
#
# Exercise 1: Make our existing Animals class abstract.
#
# Exercise 2: Override the eat method of the parent class.
#
# Exercise 3: Extend the eat method of the parent class.
#
# HOMEWORK: Override and extend the eat method in Fox class as well.
#
# Inside Fox class
# Create a method eat
#    - Add a print statement telling what might a fox eat.
#    - Use super() to call the eat method of the parent class.
#
########################################

# class Animals():
#   def __init__(self, name):
#     self.name = name
#     self.weight = ""
#     print("<p>Name: ", name, "</p>")
#
#   def eat(self):
#     print("<p>",self.name, 'is eating now..', "</p>")
#
# class Dogs(Animals):
#   def __init__(self, name, breed):
#     super(Dogs, self).__init__(name)
#     self.breed = breed
#     print("<p>", name, "is of breed", breed, "</p>")
#
#   def speak(self):
#     print("Dog: <audio src=woof.mp3 controls></audio> ")
#
#
# class Cats(Animals):
#   def speak(self):
#     print("Cat: <audio src=meow.mp3 controls></audio> ")
#
#
# class Fox(Animals):
#   def speak(self):
#     print("Fox: <audio src=blah.mp3 controls></audio> ")
#
# dog1 = Dogs("Shelby", "bulldog")
# cat1 = Cats("Charlie")
# fox1 = Fox("Firefox")
#
# fox1.speak()
# dog1.speak()
# cat1.speak()
#
# fox1.eat()
# dog1.eat()
# cat1.eat()

class Animal(ABC):
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  async def eat(self):
    self.weight+=10
    print(self.name + "is eating now... He is now "+str(self.weight)+" pounds.")
    await asyncio.sleep(1)
    print("HEHEEEEE")

  def info(self):
    print(self.name+" is a "+self.__class__.__name__+" who weighs "+str(self.weight)+" pounds.")

  @abstractmethod
  def speak():
    pass


class Dog(Animal):
  def __init__(self, name, weight):
    super().__init__(name, weight)

  def speak(self):
    print("<audio src='woof.mp3' autoplay></audio>")

class Cat(Animal):
  def __init__(self, name, weight):
    super().__init__(name, weight)

  def speak(self):
    print("<audio src='meow.mp3' autoplay></audio>")

dog1 = Dog("Woofy", 56)
cat1 = Cat("Kittens", 101)

# dog1.eat()
cat1.speak()

loop = asyncio.get_event_loop()
loop.run_until_complete(dog1.eat())
