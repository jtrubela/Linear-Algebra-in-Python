# #############################################################################################
#   Dr. Song AMAT 240 (Intro. to Linear Algebra) Fall 2022 1       #Project 1 
#
#   Group 5 - Joe Verdi and Justin Trubela                         #October 2022
#
#   Purpose: Draw Lower Case Letter k
#
#       The lower case letter k is shown in Figure 1. As can be seen, the letter is determined 
#       by a set of vertices. In this project, you will use matrices, transformations and 
#       Python program to draw different lower case k.
#
#       Questions
#       1. (5 pts) Design vertices of the lower case k.
#       2. (5 pts) What is the adjacency matrix?
#       3. (10 pts) Using Python program to draw the lower case k.
#       4. (10 pts) Rotate the lower case k by 45◦counterclockwise around the lower left corner,
#           then use a linear transformation to draw the rotated k.
#       5. (10 pts) Using a linear transformation to draw the backwards lower case k.
#
# #############################################################################################

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show

#  ??FUNCTION??
#
#def PlotVertices():
#    plt.subplots(1)
# return 


# Q1: (5 pts) Design vertices of the lower case k
kMatrix = np.array([[0, 5, 5, 10, 15,    9, 15, 10,  5,  5,  0],
                    [0, 0, 9,  0,  0, 10.5, 20, 20, 12, 25, 25]])


# Q2: (5 pts) The adjacency matrix of the lower case k
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

# Q3: (10 pts) Draw lower case k using Python
fig, k1 = plt.subplots(1)                       #declare figure and list[Axes]

for row in range(11):                           
    for column in range(row):
        if adjMatrix[row, column] == 1:         #if the adjacency matrix for current row, col is 1
            k1.plot([kMatrix[0,    row],               #plot a vertice
                     kMatrix[0, column]],
                    [kMatrix[1,    row],
                     kMatrix[1, column]], 
                    'black')                    
k1.axis('off')                                  


# Q4: (10 pts) Rotate the lower case k by 45° counterclockwise around
# the lower left corner, then use a linear transformation to draw the rotated k.
theta = math.pi / 3                   #45° CCW ≈ 225° CW---\--------------------|
                                                            # R_𝜭=[cos𝜭 -sin𝜭;  |
# Rotation Matrix                                           #     sin𝜭  cos𝜭],  | 
rotation = np.array([[math.cos(45), -math.sin(45)],         #-------------------|
                     [math.sin(theta), math.cos(theta)]])

kRotated = np.matmul(rotation, kMatrix)                     #Matrix Multiplication

fig, k4 = plt.subplots(1)                                   #Declare figure and list[Axes]

for row in range(11):
    for column in range(row):
        if adjMatrix[row, column] == 1:
            k4.plot([kRotated[0,    row], 
                     kRotated[0, column]], 
                    [kRotated[1,    row], 
                     kRotated[1, column]], 
                    'black')
k4.axis('off')


# Q5: (10 pts) Use linear transformation to draw backwards lowercase 'k'
transformation = np.array([[-1, 0], [0, 1]])
kTransformed = np.matmul(transformation, kMatrix)
fig, k5 = plt.subplots(1)
for row in range(11):
    for column in range(row):
        if adjMatrix[row, column] == 1:
            k5.plot([kTransformed[0, row], kTransformed[0, column]], [kTransformed[1, row], kTransformed[1, column]], 'black')
k5.axis('off')

show()
