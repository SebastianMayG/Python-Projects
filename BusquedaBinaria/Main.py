from BusquedaBinaria import BusquedaBinaria

busqueda = BusquedaBinaria

class Main:
    array = []

    for i in range (0,20,2):
        array.append(i)
    
    print(array)

    x = int(input("¿Que numero desea buscar? "))

    print("Esta en la posicion" ,BusquedaBinaria.Busqueda_Binaria(array,x))
