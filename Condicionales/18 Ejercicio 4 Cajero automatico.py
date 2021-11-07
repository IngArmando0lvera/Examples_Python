'''Ejercicio 4
Crear un programa que simule un cajero automatico con un 
saldo inicial de $2000, con el siguiente menú:
1.- Ingrese dinero
2.- Retirar dinero
3.- Mostrar saldo
4.- Salir
'''

saldo=2000
from os import system #libreria para ejecutar codigo batch
from time import sleep #libreria para generar retraso
menuBandera=1

while menuBandera==1:
    bandera=1
 
    system("cls")
    print("")
    print("1.- Ingrese dinero")
    print("2.- Retirar dinero")
    print("3.- Mostrar saldo")
    print("4.- Salir")
    seleccion = int(input("\nSeleccione una opcion:"))
   

    if seleccion==1:
        while bandera==1:
            entrada=float(input("Ingrese la cantidad a depositar:"))
            if entrada<=0:
                print("Entrada no valida!, ingrese cantidad valida.")
                sleep(2)
                print("\n\n")
                
            else:
                bandera=0
                saldo+=entrada
                print(f"Saldo agragado: {entrada}")
                sleep(2)

    elif seleccion==2:
        while bandera==1:
            salida=float(input("Ingrese cantidad a retirar:"))
            if salida>saldo:
                print("Operacion no exitosa.")
            else:
                bandera=0
                saldo-=salida
                print(f"Efectivo despachado: {salida}, saldo existente: {saldo}")
                sleep(3)
    elif seleccion==3:
        print("--------------------------------")
        print(f"Su saldo es: {saldo}")
        print("--------------------------------")
        sleep(3)

    elif seleccion==4:
        system("cls")
        print("Gracias por usar el cajero")
        menuBandera=0
    else:
        input("\n\nOpcion invalida, intentelo nuevamente.")
        system("cls")


