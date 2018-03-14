#Max Low
#3-14-18
#rocket2.py -- escape velocity simulation

from ggrocket import Rocket, Planet
from math import radians, sqrt

Re = 6.371E6
Me = 5.972E24
G = 6.674E-11

Ve = sqrt(2*Me*G/Re)

print("predicted escape velocity is", Ve, "m/s")

earth = Planet(viewscale=0.000009)
rocket = Rocket(earth, heading= radians(90), directiond=90, velocity=Ve, timezoom=2)
earth.run(rocket)
