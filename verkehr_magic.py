#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

GRIDSIZE = 300
INIT_CELLS = int(GRIDSIZE*0.25)
MAX_TIME = 300
EMPTY_CELL = -1
Dally = 0.2

# query distance between two cars
def get_distance(grid, i):
    dist = 6
    # Compute distance between current position and next car
    # no car = -1
    # car = 1
    for j in range(i+1, GRIDSIZE):
        if grid[j] != EMPTY_CELL:
            dist = j - i
            break
    return dist

# state transition t -> t + dt
def update(grid_old, grid_new):
    for i in range(GRIDSIZE):
        dist = get_distance(grid_old, i)
        if grid_old[i] != EMPTY_CELL:

            #Beschleunigung
            #v =  min old_grid + 1, v max
            v = min(grid_old[i] + 1, 5)

            #Bremsen
            # v = d(i,i+1) falls v>d(i,i+1)
            v = min(v, dist-1)

            #Trödeln
            #v = max(v-1, 0) mit 0.5 Wahrscheinlichkeit p <1
            p = np.random.random()
            if p < Dally:
                v = max(v-1, 0)

            # Bewegen
            grid_new[(i+v)%GRIDSIZE] = v
    
# allocate memory and initialise grids
grid_old = np.full((GRIDSIZE), EMPTY_CELL, dtype=np.int32)
grid_new = np.full((GRIDSIZE), EMPTY_CELL, dtype=np.int32)
traffic = np.zeros((MAX_TIME, GRIDSIZE), dtype=np.int32)

# set intial car positions and velocities
for k in range(INIT_CELLS):
    while True:
        i = int(float(GRIDSIZE)*np.random.random())
        if grid_old[i] == EMPTY_CELL:
            grid_old[i] = int(float(6)*np.random.random())
            break

# run updates
for t in range(MAX_TIME):
    traffic[t,:] = grid_old[:]
    update(grid_old, grid_new)
    for i in range(GRIDSIZE):
        grid_old[i] = grid_new[i]
        grid_new[i] = EMPTY_CELL
plt.xlabel('Cells')
plt.ylabel('Timesteps')
plt.imshow(traffic, cmap='Blues')
plt.show()
