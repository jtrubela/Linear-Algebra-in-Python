#Project 1 
#Justin Trubela and Joe Verdi
#Purpose: Demonstrates plotting using matrices


import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show


# Q1: Design the vertices of the lower case k
kMatrix = np.array([[0, 5, 5, 10, 15, 9,    15, 10, 5,  5,  0],
                    [0, 0, 9, 0,  0,  10.5, 20, 20, 12, 25, 25]])


# Q2: The adjacency matrix of the lower case k
# Maps edge connection of each vertex
adjMatrix = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])


# Q3: Draw lower case k using Python
fig, k1 = plt.subplots(1)
for row in range(11):
    for column in range(row):
        if adjMatrix[row, column] == 1:
            k1.plot([kMatrix[0, row], kMatrix[0, column]], [kMatrix[1, row], kMatrix[1, column]], 'black')
k1.axis('off')


# Q4: Rotate the lower case k by 45() counterclockwise around
# the lower left corner, then use a linear transformation to draw the rotated k.
theta = math.pi / 3

# Matrix used for rotation
rotation = np.array([[math.cos(45), -math.sin(45)],
                     [math.sin(theta), math.cos(theta)]])
kRotated = np.matmul(rotation, kMatrix)
fig, k4 = plt.subplots(1)
for row in range(11):
    for column in range(row):
        if adjMatrix[row, column] == 1:
            k4.plot([kRotated[0, row], kRotated[0, column]], [kRotated[1, row], kRotated[1, column]], 'black')
k4.axis('off')


# Q5 Use linear transformation to draw backwards lowercase 'k'
transformation = np.array([[-1, 0], [0, 1]])
kTransformed = np.matmul(transformation, kMatrix)
fig, k5 = plt.subplots(1)
for row in range(11):
    for column in range(row):
        if adjMatrix[row, column] == 1:
            k5.plot([kTransformed[0, row], kTransformed[0, column]], [kTransformed[1, row], kTransformed[1, column]], 'black')
k5.axis('off')

show()
