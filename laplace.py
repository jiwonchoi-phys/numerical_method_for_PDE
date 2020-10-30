# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 11:14:40 2020

@author: jiwon
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np


# Size of grid
N = 40

# Initialize grid(packed with 0)
grid = np.zeros((N+2,N+2))


step = 500

ax = 5
ay = 5
hx = ax/(N-1)
hy = ay/(N-1)
x = np.linspace(0,ax,N+2)
y = np.linspace(0,ay,N+2)

# Give boundary condition
for i in range(N+2):
    
    grid[0,i] = 5
    grid[N+1,i] = 5
    
# Initial grid
print(grid)


# iteration function
def iteration():
    for i in range(N):
        for j in range(N):
            grid[i+1,j+1] = (grid[i+2,j+1] + grid[i,j+1] + \
                grid[i+1,j+2] + grid[i+1,j])/4
    
        grid[20,20] = 10


# Iterate grid
for i in range(step):
    iteration()


# Plot
hf = plt.figure()
ha = hf.add_subplot(111,projection='3d')

X, Y = np.meshgrid(x,y)
ha.plot_surface(X,Y,grid,cmap=cm.coolwarm)
plt.show()
plt.savefig("laplace equation", dpi=300)


# Output grid
print(grid)