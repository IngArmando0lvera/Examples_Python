array =["futbool", "pc", "pc", 18, 16, [2, 3, 5], True, False] #Array

repeticion=array.count("pc")
print(repeticion)#cuenta las veces que se repite

array.remove("pc")
print(array)

array.clear()
print(array)


array.extend(["futbool", "pc", "pc", 18, 16, [2, 3, 5], True, False])
print(array)


array.reverse()
print(array)

array2=[1,3,7,2,8,55,4,33,4,77,99,123,443,5,2,443,32,23,14,11,97,2344]
array2.sort()
print(array2)

array2.sort(reverse=True) #ordena de mayor a menor
print(array2)