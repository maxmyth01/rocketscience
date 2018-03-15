#Max Low
#3-15-18
#rocket3.py -- getting into orbit with realistice thrust

from ggrocket import Rocket, Planet
from math import radians, sqrt, log
from ggmath import InputButton, Timer

earth = Planet(planetass=0) # no gavity for simplification

RocketStarted = False
StartTime = None # to keep track of when burn started
BurnTime = 0 # how long burn has lasted

# Falcon F9R specifications
me = 25600  # empty mass
mp = 395700  #propellent mass
F1D = 716000    # single engine thrust (N)
N1D =9    #Number of rocket engines

Ftotal = F1D * N1D  # total thrust (N)
tburn = 180  # burn time

# Predict the final vleocity based on N's 2nd law
vmax = Ftotal*tburn/(me+mp)
print("predicted final velocity (N's 2nd law), vmax: ", vmax, "m/s")

def GetThrust():
    global BurnTime
    global RocketStarted
    if RocketStarted:
        BurnTime = rocket.shiptime - StartTime
        if burnTime >= tburn:
            RocketStarted = False
            return 0
        else:
            return Ftotal
    else:
        return 0
    
def StartRocket():
    global RocketStarted
    global StartTime
    if not RocketStarted = True
    StartTime = rocket.shiptime
    
start = InputButton((10,400), "Start", StartRocket, positioning="physical", size=15)

rocket = Rocket(earth, thrust=GetThrust, mass=mp+me)
earth.run(rocket)
    
