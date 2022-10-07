# 2D-stellar-random-walk-simulation

This is a simple 2D simulation that simulates the random walking motion of the photons in a star.
With every step, each photon moves the distance equivalent to mean displacement in timestep [m], in a randomly chosen direction. 

[INPUT]
You need to manually put in the time step [yr], mean displacement in timestep [m], stellar radius [m], and number of photons to simulate [#].
* You can calculate the mean displacement in timestep with d = l sqrt(N) (l: mean free path, N: approximated number of random steps in the timestep)

[OUTPUT]
The code outputs a real-time visualisation of the evolving system.
The title of the plot shows the time elapsed, mean distance of the photons from the center, and the number of photons that had escaped the atmosphere. Every time a photon escapes the star, the time elapsed before the photon was liberated is printed. 

Simple average all printed outputs to approximate the time it takes for the average photon to escape the star.
