from Operaciones import Resta, Suma, Multiplicacion, Division, Potencia

while True:
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- Division")
    print("5.- Potencia")
    print("6.- Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        a = float(input("Dame el primer número: "))
        b = float(input("Dame el segundo número: "))
        print("La suma es: " , Suma(a , b))

    elif opcion == 2:
        a = float(input("Dame el primer número: "))
        b = float(input("Dame el segundo número: "))
        print("La resta es :" , Resta(a , b))

    elif opcion == 3:
        a = float(input("Dame el primer número: "))
        b = float(input("Dame el segundo número: "))
        print("La multiplicación es: " , Multiplicacion(a , b))

    elif opcion == 4:
        a = int(input("Dame el primer número: "))
        b = int(input("Dame el segundo número: "))
        print("El cociente es: " , Division(a , b))

    elif opcion == 5:
        a = float(input("Dame la base: "))
        b = float(input("Dame el exponente: "))
        print("El resultado es: " , Potencia(a , b))

    elif opcion == 6:
        print("Saliendo...")
        break

    else:
        print("Elige una opción correcta :)")
        break
