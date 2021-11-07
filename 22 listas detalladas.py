array =["futbool", "pc", 18, 16, [2, 3, 5], True, False]

array.append(66)    #agregar datos al final
array.append(True)

array.insert(1,88) #indice 1, registro (dato)

array.extend([1, 88, True, 100]) #Agregamos elementos al final de la lista





print("lista:    ",array)
print("longitud:   ",len(array))

'''Concatenando listas'''
array2=[200, 250, "hola"]
array3=array+array2
print("--------------------------------")
print(array3)