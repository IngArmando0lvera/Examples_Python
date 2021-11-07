'''Ejercicio N.3
Crea un programa  que compare dos nombres, y verificar si hay coincidencias o no,
si es que ambos nombres comienzan con la misma letra o si terminan con la misma
letra.
'''

#ingresamos los nombres.
nombre1 = input("\n\nNombre 1:")
nombre2 = input("Nombre 2:")

#proceso
if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print("Si hay coincidencias")
else:
    print("No hay coincidencias")




