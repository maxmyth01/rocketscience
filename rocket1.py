#Max Low
#3-14-18
#rocket1.py -- first rocket orbital program safe altitude

from ggrocket import Rocket, Planet

earth = Planet()
rocket = Rocket(earth)
earth.run(rocket)
