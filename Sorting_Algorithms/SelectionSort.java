package Sorting_Algorithms;

public class SelectionSort {

    public static void selectionSort(int[] array) {

        for (int i = 0; i < array.length; i++) {
    
            // run through the unsorted elements in the input, finding
            // the smallest one.
            int smallestIndex = i;
            for (int j = i + 1; j < array.length; j++) {
                if (array[j] < array[smallestIndex]) {
                    smallestIndex = j;
                }
            }
    
            // move the smallest element to the front of the unsorted portion
            // of the input (swapping with whatever's already there).
            int temp = array[smallestIndex];
            array[smallestIndex] = array[i];
            array[i] = temp;
        }
    }
    
}
