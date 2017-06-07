#!/usr/bin/python

from PyGlow import PyGlow
from time import sleep
from datetime import datetime

pyglow = PyGlow()
pyglow.all(0)

all_colours = ["white","blue","green","yellow","orange","red"]

for i in range(5): 
  for colour in all_colours:
    pyglow.color(colour, 100)
    sleep(0.1)
    pyglow.all(0)
