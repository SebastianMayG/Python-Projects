class BusquedaBinaria:
    
    def Busqueda_Binaria(array,x):
        inicio = 0
        final = len(array)-1

        while(inicio <= final):
            centro = (inicio + final)//2

            if(array[centro] == x):
                return centro
            elif(array[centro] < x):
                inicio = centro + 1
            elif(array[centro] > x):
                final = centro -1

        return -1