#!/usr/bin/python3.5
print("Content-Type:text/html")
print()

import secrets

import cgitb
cgitb.enable()
# THIS IS FOR PYTHON 3.6, SO WILL NOT WORK ON CODEWIZARDS

class Keyboard():
  def __init__(self, brand, language):
    self.brand = brand
    self.language = language
    self.secret = secrets.randbelow(999999999)

  def type(self, msg):
    print(f"<p>[{self.secret}]: {msg}</p>")

class Monitor():
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def play(self, video):
    print(f"<video src={video} controls></video>")


class Computer():
  def __init__(self, keyboard, screen):
    self.os = "StoneOS"
    self.processor = "Dirt-9000X"
    self.keyboard = keyboard
    self.screen = screen

keyboard = Keyboard("Poop Co™", "Engliso")
monitor = Monitor("300","300")

computer = Computer(keyboiard, monitor)
computer.keyboard.type("hajkldsfhasdlkfjhasdkljf")
computer.screen.play("kite.ogv")
