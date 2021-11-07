'''Ejercicio N.1
Crear un programa que pida 2 numeros y obtener como resultado
cual de ellos es par o si ambos son par
'''

#obtenemos datos
dato1 = int(input("Ingrese dato 1: "))
dato2 = int(input("Ingrese dato 2: "))


#procesamos 

if dato1%2 == 0 and dato2%2 == 0:
    print("Ambos datos son par!")
elif dato1%2 == 0:
    print("Dato 1 es par!")
elif dato2%2 == 0:
    print("Dato 2 es par!")
else:
    print("Ninguno es par!")
