#!/usr/bin/python

from PyGlow import PyGlow
from time import sleep
from datetime import datetime
# List all colours
all_colours = ["white","blue","green","yellow","orange","red"]

# instantiate the PyGlow API
pyglow = PyGlow()
# Clear the current status
pyglow.all(0)

def notify_glow(num_pulses, in_colours):
  for i in range(num_pulses):
    for colour in in_colours:
      pyglow.color(colour, 100)
      sleep(0.1)
      pyglow.all(0)

def main():
  # Test glow with all colours
  notify_glow(5,all_colours)

if __name__ == "__main__":
  main()
