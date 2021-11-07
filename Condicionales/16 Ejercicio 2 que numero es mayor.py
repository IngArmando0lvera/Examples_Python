'''Ejercicio 2 
Crear un programa que pida 3 numeros y determine 
cual es el mayor
'''

numero1=float(input("Ingrese primer numero: "))
numero2=float(input("Ingrese segundo numero: "))
numero3=float(input("Ingrese tercer numero: "))

#proceso

if numero1>numero2:
    if numero1>numero3:
        print(f"El numero mayor es 1: {numero1}")
    else:
        print(f"El numero mayor es 3: {numero3}")
else:
    if numero2>numero3:
        print(f"El numero mayor es 2: {numero2}")
    else:
        print(f"El numero mayor es 3: {numero3}")
        

