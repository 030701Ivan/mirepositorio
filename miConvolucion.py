import numpy as np

#Funciónq ue calcula la matriz resultante c despuñes de aplicar la operación convolución de A*B
def convolución(A,B):
	C = 0
	return C

matriz1 = [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
filtro = [[1,0,2],[5,0,9],[6,2,1]]

A = np.array(matriz1)
B = np.array(filtro)
C = np.zeros((2,2))
#print(A)

#Para imprimir un valor en específico de mi matriz
#Primero filas y luego columnas 
#En python se empieza desde 0
#print(A[1][0])

#print(C)

#B[0][0]+B[0][1]+B[0][2]+B[1][0]+B[1][1]+B[1][2]+B[2][0]+B[2][1]+B[2][2]

SA1  = A[0][0]*B[0][0]+A[0][1]*B[0][1]+A[0][2]*B[0][2]+A[1][0]*B[1][0]+A[1][1]*B[1][1]+A[1][2]*B[1][2]+A[2][0]*B[2][0]+A[2][1]*B[2][1]+A[2][2]*B[2][2]
SA2 = A[0][1]*B[0][0]+A[0][2]*B[0][1]+A[0][3]*B[0][2]+A[1][1]*B[1][0]+A[1][2]*B[1][1]+A[1][3]*B[1][2]+A[2][1]*B[2][0]+A[2][2]*B[2][1]+A[2][3]*B[2][2]
SA3 = A[1][0]*B[0][0]+A[1][1]*B[0][1]+A[1][2]*B[0][2]+A[2][0]*B[1][0]+A[2][1]*B[1][1]+A[2][2]*B[1][2]+A[3][0]*B[2][0]+A[3][1]*B[2][1]+A[3][2]*B[2][2]
SA4 = A[1][1]*B[0][0]+A[1][2]*B[0][1]+A[1][3]*B[0][2]+A[2][1]*B[1][0]+A[2][2]*B[1][1]+A[2][3]*B[1][2]+A[3][1]*B[2][0]+A[3][2]*B[2][1]+A[3][3]*B[2][2]

C[0][0] = SA1
C[0][1] = SA2
C[1][0] = SA3
C[1][1] = SA4

print(C)
