import numpy as np


#1
matrix = np.array([[6,-9,1],[4,24,8]])
scalar = 2

matrix_scalar_product = matrix * scalar
print(matrix_scalar_product)


#2
matrix_1 = np.array([[1,0],[0,1]])

dot_product = np.dot(matrix_1, matrix)
print(dot_product)

#3 

matrice_1 = np.array([[4,3],[3,2]])
matrice_2 = np.array([[-2,3],[3,-4]])

dot_product2= np.dot(matrice_1,matrice_2)
print(dot_product2)