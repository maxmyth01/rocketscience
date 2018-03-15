#Max Low
#3-15-18
#rocket3.py -- getting into orbit with realistice thrust

from ggrocket import Rocket, Planet
from math import radians, sqrt, log
from ggmath import InputButton, Timer, Slider

earth = Planet(planetmass=0, viewscale = 0.000005) # no gavity for simplification

RocketStarted = False
StartTime = None # to keep track of when burn started
BurnTime = 0 # how long burn has lasted

# Falcon F9R specifications
me = 25600  # empty mass
mp = 395700  #propellent mass
F1D = 716000    # single engine thrust (N)
N1D =9    #Number of rocket engines

Ftotal = F1D*N1D  # total thrust (N)
tburn = 180  # burn time

# Predict the final vleocity based on N's 2nd law
vmax = Ftotal*tburn/(me+mp)
print("predicted final velocity (N's 2nd law), vmax: ", vmax, "m/s")

# Vfianl based on Tsiolkovsky's Rocket Equation
vmaxre = Ftotal*tburn/mp*log((me+mp)/me)
print("Predicted final velocity (rocket Eqation), vmax: ",vmaxre, "m/s")

def GetThrust():
    global BurnTime
    global RocketStarted
    if RocketStarted:
        BurnTime = rocket.shiptime - StartTime
        if BurnTime >= tburn:
            RocketStarted = False
            return 0
        else:
            return Ftotal
    else:
        return 0
    
def StartRocket():
    global RocketStarted
    global StartTime
    if not RocketStarted:
        RocketStarted= True
        StartTime = rocket.shiptime
        
def GetMass():
    global RocketStarted
    if RocketStarted:
        return me + mp*(tburn-BurnTime)/tburn
    else:
        return me +mp


tz = Slider((10,400), 0, 5, 0, positioning="physical")    
start = InputButton((10,500), "START", StartRocket, positioning="physical", size=15)

rocket = Rocket(earth, thrust=GetThrust, timezoom = tz, mass=GetMass)
earth.run(rocket)
    
