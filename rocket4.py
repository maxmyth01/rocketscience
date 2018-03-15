#Max Low
#3-15-18
#rocket4.py -- 2 stage rocket simulation

from ggrocket import Rocket, Planet
from math import radians, sqrt, log
from ggmath import InputButton, Timer, Label, Slider

earth = Planet(planetmass=0)

Stage1Started = False
Stage2Started = False
PayloadLaunched = False
StartTime = None
BurnTime = 0

me1 = 25600
mp1 = 395700
Ftotal1 = 6.444E6
tburn = 180

me2 = 3900
mp2 = 92670
Ftotal2 = 8.01E5
tburn2 = 372

mep = 13150

vmax1 = Ftotal1*tburn/mp1*log((me1+mp1+me2+mp2+mep)/(me1+me2+mp2+mep))
vmax2 = Ftotal2*tburn/mp2*log((me2+mp2+mep)/(me2+mep))

print("predicted final staged rocket velocity (Rocket Equation), vmax:", vmax1+vmax2, "m/s")

def GetThrust():
    global StartTime
    global BurnTime
    global Stage1Started
    global Stage2Started
    global PayloadLaunched
    if Stage1Started:
        tburn = tburn1
        Ftotal = Ftotal1
    elif Stage2Started:
        tburn = tburn2
        Ftotal = Ftotal2
    if Stage1Started or Stage2Started:
        BurnTime = rocket.shiptime - StartTime
        if BurnTime >= tburn:
            if Stage1Started:
                Stage1Started = False
                Stage2Started = True
                StartTime = rocket.shiptime
                return Ftotal2
            else:
                Stage2Started = False
                PayloadLaunched = True
                return 0
        else:
            return Ftotal
    else:
        return 0
        

def StartRocket():
    global Stage1Started
    global StartTime
    if not (Stage1Started or Stage2Started):
        Stage1Started = True
        StartTime = roket.shiptime
        
        
def GetMass():
    global Stage1Started
    global Stage2Started
    global PayloadLaunched
    if Stage1Started:
        return me1 + me2+mep + mp2+mp1*(tburn1-BurnTime)/tburn1
    elif Stage2Started:
        return me2 +mep + mp2*(tburn2-BurnTime)/tburn2
    elif PayloadLaunched:
        return mep
    else:
        return me1+mp1+me2+mp2+mep
        
def GetStatus():
    global Stage1Started
    global Stage2Started
    global PayloadLaunched
    if Stage1Started:
        return "STAGE 1 FIRING"
    elif Stage2Started:
        return "STAGE 2 Firing"
    elif PayloadLaunched:
        return "PAYLOAD DELIVERED"
    else:
        return "WAITING FOR LAUNCH"
        
start = InputButton((10,400), "START", StartRocket, positioning="physical", size=15)

Status = Label((10,420), GetStatus, positioning="physical", size=15)

tz = Slider((10,360), 0,5,0,positioning="physical")

rocket= Rocket(earth,thrust=GetThrust, mass=GetMass, timezoom=tz)
earth.run(rocket)