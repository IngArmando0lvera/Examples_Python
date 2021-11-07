'''Ejercicio N1.
Pasar la ecuacion a una expresion algoritmica'''

print("\n\n Este programa calcula el valor de salida de la siguiente ecuacion.")
print("(c+5)((b**2)-(3*a*c))(a**2)/(4*a)\n")

a = float(input("a? :"))
b = float(input("b? :"))
c = float(input("c? :"))

r = (c+5)*((b**2)-(3*a*c))*(a**2)/(4*a)

print(f"\nEl resultado es: {r}")