#Max Low
#3-14-18
#rocket2.py -- escape velocity simulation

from ggrocket import Rocket, Planet
from math import radians

earth = Planet()
rocket = Rocket(earth, heading= radians(90), directiond=90, velocity=11190)
earth.run(rocket)
