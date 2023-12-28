
class QuickSort:

    def Quick_Sort(array,primero,ultimo):
        i = primero
        j = ultimo

        centro = (primero + ultimo) // 2
        pivote = array[centro]

        while(i <= j):
            while(array[i] < pivote):
                i += 1
            while(array[j] > pivote):
                j -= 1
            if(i <= j):
                array[i],array[j] = array[j],array[i]
                i += 1
                j -= 1
        
        if(primero < j):
            QuickSort.Quick_Sort(array,primero,j)
        if(i < ultimo):
            QuickSort.Quick_Sort(array,i,ultimo)

        return array


            