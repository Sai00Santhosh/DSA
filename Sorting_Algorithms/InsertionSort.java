package Sorting_Algorithms;

public class InsertionSort {

    public static void insertionSort(int[] array){

        for (int i = 1; i < array.length; i++){

            int empty = array[i];
            int j = i - 1;

            while (j >= 0 && empty < array[j]){
                array[j + 1] = array[j];
                j = j - 1;
            }
            array[j + 1] = empty;

        }
    }
    
}
