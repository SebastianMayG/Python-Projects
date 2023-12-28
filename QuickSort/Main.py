from QuickSort import QuickSort

class Main:
    array = [9, 5, 3, 7, 2, 8, 4, 1, 6]

    print (array)

    resultado = QuickSort.Quick_Sort(array,0,len(array) - 1)

    print("arreglo ordenado es: " , resultado)
