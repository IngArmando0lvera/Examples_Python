'''Ejercicio 2 
Crear un programa que pida 3 numeros y determine 
cual es el mayor
'''

numero1=float(input("Ingrese primer numero: "))
numero2=float(input("Ingrese segundo numero: "))
numero3=float(input("Ingrese tercer numero: "))

#proceso
if numero1>numero2 and numero1>numero3:
    print(f"El primer numero es el mayor: {numero1}")
elif numero2>numero1 and numero2>numero3:
    print(f"El segundo numero es el mayor: {numero2}")
elif numero3>numero1 and numero3>numero2:
    print(f"El tercer numero es el mayor: {numero3}")
