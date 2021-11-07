'''Ejercicio N.3
Obtener el radio de un circulo y calcular el area y perimetro

'''
from math import pi

radio = float(input("\n\nIngrese el radio: "))#pedimos el radio del circulo

#Realizamos el calculo 

area = pi*radio**2
perimetro = 2*pi*radio

print(f"\n\nEl radio es {area:.2f} y el perimetro es {perimetro:.2f}\n\n")


