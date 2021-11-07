'''El presente programa muestra como buscar en listas'''

array =["futbool", "pc", "pc", 18, 16, [2, 3, 5], True, False] #Array
print(f"\n\nARRAY:{array}\n")



existe= "pc" in array #busca en la lista

print("La palabra pc esta en el array?:  ", existe)

print("pc"in array)
print(array.count("pc"))#cuenta nuemro de veces encontrado






'''Ejecutando un programa funcional'''
'''Este programa pide un dato que despues buscará en una lista'''
print("----------------------------------------------------")
array =["futbool", "pc", "pc", 18, 16, [2, 3, 5], True, False] #Array
print("Array: ",array)

busqueda=input("Ingrese dato a buscar: ")#ingresamos dato a buscar

encontrado=busqueda in array#buscamos dato en array

if encontrado==True:
    print("Dato encontrado!")
else:
    print("Dato no encontrado :(")

print(f"Y se repite {array.count(busqueda)}")