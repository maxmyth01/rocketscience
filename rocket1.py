#Max Low
#3-14-18
#rocket1.py -- first rocket orbital program safe altitude

from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.000009)
rocket = Rocket(earth, altitude=2000000, velocity=69000, timezoom=3)
earth.run(rocket)
