import numpy as np
import numpy.matlib
import sympy
from numpy import *
from numpy.linalg import matrix_power
from numpy.linalg import inv
from sympy import *
import sys
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show

#|A| = ad-bc
#A^-1 = 1/|A| adjA
#adjA = A^-1/ad-bc

#Aij = (-1)i+j det Mij


#ColA
#rref A

#dim/basis for col A if A = [a,a,a,a,a]
#  #pivot columns in A # basic variables in Ax=0 
#  a1,a2,a3 = 3     #    a1=[col],a2=[col]



#NulA
#dim/basis for Nul A
#  #nonpivot columns in A # free variables in Ax=0 
#nulA span{v1,v2}



def multiplyMatrix(A,B):
    matrix = np.matmul(A,B)
    return matrix 

def expMatrix(A, n):
    matrix = matrix_power(A,n)
    return matrix

def det(A):
    determinant = np.linalg.det(A)
    return determinant
    
def inverseMatrix(A):
    if detMatrix(A) != 0:
        ainv = inv(A)
    return ainv


#Block upper/#Block Lower
#partition -> determinants -> multiply -> 

def transpose(A):
    matrix = np.transpose(x)
    return matrix

def rrefMatrix(A):
    matrix = A.rref()
    return matrix

def projection(b,c,d,x,y,z):
    xyz = 1
    A = np.array([[1,0,(-b/d),0],[0,1,(-c/d),0],[0,0,0,0],[0,0,(-1/d),1]])
    cop = np.array([[x],[y],[z],[xyz]])
    A_xyz = np.matmul(A,cop)

    a = ((-1/d)*(z))+(d/d)
    numerator = a*d
    denominator = d

    a_x = (denominator/numerator) * A_xyz[0]
    a_y = (denominator/numerator) * A_xyz[1]
    
    print("a=",a_x)
    print("b=",a_y)
    print("0",0)
    
   
#3A = 3*|A|
#any 2 rows or cols are == then it  = 0

'''
If A is a non-singular matrix i.e., |A| ≠ 0, then its inverse exists.
We have A X = B
or, A– 1 (A X) = A– 1 B (pre-multiplying by A– 1)
or, (A– 1 A) X = A– 1 B
and, I X  = A– 1 B (I is the identity matrix)
or, X = A– 1 B where,  A– 1 = (adj A) ⁄ |A|
This matrix equation provides a unique solution and is known as the Matrix Method.'''
 
    
def rotate(matrix, axis, degrees):
    phi=(degrees*(math.pi/180))
    cos=math.cos(phi)
    sin=math.sin(phi)

    if axis=='y': 
        yRotate = np.array([[ cos, 0, sin, 0],[0, 1, 0, 0],[-sin, 0, cos, 0],[0, 0, 0, 1]])
        rotatedMatrix = np.matmul(yRotate,matrix)
        return rotatedMatrix
    elif axis=='z':
        zRotate = np.array([[cos, -cos, 0, 0],[cos, cos, 0, 0],[0, 0, 1, 0],[0,0, 0, 1]])
        rotatedMatrix = np.matmul(zRotate, matrix)
        return rotatedMatrix
    else:
        return matrix
    


# def matrix_cofactor(matrix):
 
#     try:
#         determinant = np.linalg.det(matrix)
#         if(determinant!=0):
#             cofactor = None
#             cofactor = np.linalg.inv(matrix).T * determinant
#             # return cofactor matrix of the given matrix
#             return cofactor
#         else:
#             raise Exception("singular matrix")
#     except Exception as e:
#         print("could not find cofactor matrix due to",e)
        
# # print(matrix_cofactor([[1, 9, 3],
# #                        [2, 5, 4],
# #                        [3, 7, 8]]))

# def solve_triangular(A,B, lower=None):
#     A = np.array(A)
#     B = np.array(B)
    
#     x = solve_triangular(A,B,lower=True)
    

    
    
    
    
#2 - Calculate AB, B^t(A-2I_3)  
#import       
A = np.array([[1,1,1],[1,2,3],[1,4,5]])
B = np.array([[2,3],[-6,7],[1,5]])

print(multiplyMatrix(A,B))
I2 = 2*np.matlib.identity(3)
print(I2)
A2I = np.subtract(A,I2)
print(A2I)
BT = B.transpose()
print(BT)
BTA2I = multiplyMatrix(BT,A2I)

print(BTA2I)




#3 - invertible matrices or not
#inv(np.array([[-2,(1/2)],[6,(1/2)],[1,0]]))
print(inv(np.array([[12,-2],[6,0.5]])))
print(inv(np.array([[18,9],[-2,-1]])))



#4 - inverse of A
print(inv(np.array([[-1,1,-1],[2,-1,1],[1,3,2]])))




#5 - find 3x3 matrix that translates vectors in r^2 by (-1,3) first then rotates the translated vectors by 30 degrees, using homogeneous coordinates




#6 - Linear Transformation T: R^2 -> R^2 by T([x1],[x2]) = ([3,-5],[4,-5])
print(np.array([[3,-5],[4,-5]]))






#7 - cofactor C32 and C41
# A = np.array([[10,-2,0,0],[3,0,1,1],[0,0,5,-2],[-2,0,6,4]])
# A11C11 = np.array([[0,1,1],[0,5,-2],[0,6,4]])
# A1C32 = np.array([[10,0,0],[3,1,1],[-2,6,4]])
# A1C41 = np.array([[-2,0,0],[0,1,1],[0,5,-2]])
# print(matrix_cofactor(A))
# print(matrix_cofactor(A1C32))
# print(matrix_cofactor(A1C41))





#8 - block upper triangular matrix
# A1 = np.array([[2,1,3],[0,5,-2],[0,4,6]])
# B1 = np.array([[2,1,3,7],[2,-1,5,7],[0,0,-2,10],[0,0,6,0]])
#9 - block lower triangular matrix
# A2 = np.array([[2,1,0],[1,5,0],[0,4,6]])
# B2 = np.array([[2,0,0],[2,-1,5],[0,10,6]])

# #a-1_22
# print(inv(np.array([[5,-2],[4,6]])))

# print((1/38)*(6))

# print(inv(A1))
# print(inv(B1))
# print(inv(A2))
# print(inv(B2))





#10 - (1)Find basis for Col A; (2)Find basis for Nul A; (3)Find dim Col A, dim Nul A, rank A
A = np.array([[1,2,-2,0,7],[-2,-3,1,-1,-5],[-3,-4,0,-2,-3],[3,6,-6,5,1]])
B = np.array([[1,0,4,0,-3], [0,1,-3,0,5],[0,0,0,1,-4],[0,0,0,0,0]])
   



#11. Find (a,b,0) be the image of (1,3,3) under perspective projection with cop (0,0,5)
print(projection(0,0,5,1,3,3))