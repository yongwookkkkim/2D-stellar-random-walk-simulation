# 2D-stellar-random-walk-simulation

This is a simple 2D simulation that simulates the random walking motion of the photons in a star.
With every step, each photon moves the distance equivalent to (mean free path [m] * time step [yr] * collision rate[#/s] * 31,557,600 [s/yr]), in a randomly chosen direction. 
The outer bound (the stellar boundary) has the radius of (stellar radius [m]).

[INPUT]
You need to manually put in the time step [yr], mean free path [m], stellar radius [m], number of photons too simulate [#], and collision rate [#/s].

[OUTPUT]
The code outputs a real-time visualisation of the evolving system.
The title of the plot shows the time elapsed, mean distance of the photons from the center, and the number of photons that had escaped the atmosphere. Every time a photon escapes the star, the time elapsed before the photon was liberated is printed. 

Simple average all outputs to approximate the time it takes for the average photon to escape the earth.
