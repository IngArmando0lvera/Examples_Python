'''Ejercicio 1 
Crear un programa que muestre la sumatoria de todos 
numeros entre 0 y el 100'''
suma=0
for i in range(101):
    suma+=i
    print(f"sumatoria de {i} es: {suma}")