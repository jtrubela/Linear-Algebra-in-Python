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
import numpy as np                              #https://is.gd/EkIBvK
import matplotlib.pyplot as plt                 #https://is.gd/5akTkL
from matplotlib.pyplot import plot, ion, show
# Colors for figures
red = 'r'
green = 'g'
blue = 'b'

# coordinate matrix for k
matrix = np.array([[0, 5, 5, 10, 15,    9, 15, 10,  5,  5,  0],
                   [0, 0, 9,  0,  0, 10.5, 20, 20, 12, 25, 25]])

# Q2: (5 pts) The adjacency matrix of the lower case k
# Maps edge connection of each vertex
adjacencyMatrix = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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
fig, k1 = plt.subplots(1)

# Function for drawing k
def plotFigure(figure, matrix, adjacencyMatrix, color):
    for row in range(11):                           
        for column in range(row):
            if adjacencyMatrix[row, column] == 1:
                 figure.plot([matrix[0,    row],
                              matrix[0, column]],
                             [matrix[1,    row],
                              matrix[1, column]], 
                             color)
    return figure.axis('off')

k1 = plotFigure(k1, matrix, adjacencyMatrix, green) #prints matrix

# Q4: (10 pts) Rotate the lower case k by 45° counterclockwise around
# the lower left corner, then use a linear transformation to draw the rotated k.
theta = math.pi / 3                   #45° CCW ≈ 225° CW---\--------------------|
                                                            # R_𝜭=[cos𝜭 -sin𝜭;  |
# Rotation Matrix                                           #     sin𝜭  cos𝜭],  | 
rotation = np.array([[math.cos(45), -math.sin(45)],         #-------------------|
                     [math.sin(theta), math.cos(theta)]])

kRotated = np.matmul(rotation, matrix)                     #Matrix Multiplication

fig, k4 = plt.subplots(1)
k4 = plotFigure(k4, kRotated, adjacencyMatrix, blue) #prints matrix


# Q5: (10 pts) Use linear transformation to draw backwards lowercase 'k'
transformation = np.array([[-1, 0], [0, 1]])
kTransformed = np.matmul(transformation, matrix)
fig, k5 = plt.subplots(1)
k5 = plotFigure(k5, kTransformed, adjacencyMatrix, red)

show()
