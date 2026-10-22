import numpy as np
# Mario Yañez NC 1110
# Ejemplos de numpy Numerical Python
print(" -- Espaciado Lenealmente en array -- 1110")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)
print("-- Matriz identidad en 2D array -- 1110")
matrix=np.eye(3)
print(matrix)
print("-- Genera numeros al azar(Alatorios) en 2D array -- 1110")
numale=np.random.random((3,4)) # genera 12 numeros  aleatorios
print(numale)
print("genera 9 numeros  aleatorios entre 0 y 1")
numale=np.random.random((3,3)) # genera 12 numeros  aleatorios
print(numale)
# como generar 9 numeros aleatorios comprendiendos entre 1 y 20
# con numpy en un arreglo de 3 por 3
print("genera 9 numeros  aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)

print("Mario Yañez NC 1110")