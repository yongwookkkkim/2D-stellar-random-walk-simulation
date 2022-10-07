import sys
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#CONSTANTS
c=299792458
secInYear = 31557600

#MANUAL INPUT
timeStep= 1000 #time step in years
meanFreePath= 100 #the average displacement of a photon in one timestep.
stellarRadius= 4500 #stellar radius in meters
photonNo=30 #number of photons to simulate

#DO NOT EDIT
frac = stellarRadius/meanFreePath

x_vals=np.zeros(photonNo)
y_vals=np.zeros(photonNo)
t=np.linspace(-frac,frac)
circleup=np.sqrt(frac*frac - t*t)
circledown=-np.sqrt(frac*frac - t*t)

def animate(count):
    plt.clf()
    global x_vals, y_vals
    if len(x_vals)==0:
        sys.exit("All photons escaped.")
    for i in range(len(x_vals)):
        try:
            theta=random.uniform(0,2*np.pi)
            x_vals[i] += np.cos(theta)
            y_vals[i] += np.sin(theta)
            if x_vals[i]*x_vals[i]+y_vals[i]*y_vals[i] > frac*frac:
                x_vals=np.delete(x_vals,i)
                y_vals=np.delete(y_vals,i)
                print(count*timeStep)
            plt.plot(x_vals[i], y_vals[i], marker="o")
        except IndexError:
            pass
    meandistance=0
    for k in range(len(x_vals)):
        meandistance+=np.sqrt(x_vals[k]*x_vals[k] + y_vals[k]*y_vals[k])
    meandistance /= len(x_vals)
    plt.title(f"time elapsed: {round(count*timeStep)} years \n mean distance from the center: {round(meandistance,2)} \n {photonNo-len(x_vals)} photon(s) escaped")
    plt.plot(t,circleup, color='r', linestyle='--')
    plt.plot(t,circledown, color='r', linestyle='--')

ani=FuncAnimation(plt.gcf(), animate) #interval in milliseconds, gcf=get current function

plt.xlim(-50,50)
plt.ylim(-50,50)
plt.show()