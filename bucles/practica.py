'''practica con las siguientes funciones:

    1.-    int()
    2.-    eval()
    3.-    abs()
    4.-    min()
    5.-    max()
    6.-    pow()
    7.-    round()
'''
print("\n\n")



# 1.- int
a="222"
b=int(a)  #<------
print(f"el tipo de a es {type(a)}")
print(f"el tipo de b es {type(b)}")

#2.- eval
c="23.1"
d=eval(c) #<------
print(f"-el tipo de c es {type(c)}")
print(f"-el tipo de d es {type(d)}")

#3.- abs()
e=-32233
#e=int(input("Ingrese un valor: "))
print(f"el valor obasoluto es: {abs(e)}")


#4.- min & max
array={2,3,2,4,6,2,4,6,4,3,2}
print(f"El array es: {array}")
print(f"el valor minismo es: {min(array)}")
print(f"el valor maximo es: {max(array)}")