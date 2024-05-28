// Importing arrays from the Java utility pack
import java.util.Arrays;
/**
 * Simple class to perform the Bubble Sort algorithm
 * on a given array.
 * @author Juan Carlos Cabrera
 * @version 1.0.0
 * @since Week 2 of CSC6301
 */

//  Defining main class
public class BubbleSort {
    /**
     * Main method of the class
     * @param args Default parameter for a main - not used
     * @since Week 2 of CSC6301
     */

    //  Defining main method
    public static void main(String[] args) {
        
        // Array given for us to use
        int[] myArray = {2, 45, 37, 21, 31, 50, 29, 22, 67, 88, 56};

        // Printing original array
        System.out.println("Starting unsorted array:");
        System.out.println(Arrays.toString(myArray));

        // Calling our bubblesort method 
        bubbleSort(myArray);

        // Printing sorted array
        System.out.println("Sorted Array:");
        System.out.println(Arrays.toString(myArray));
    }

    
    /** 
     * Method to repeatedly swap adjacent elements until they are in the correct order.
     * @param arr Parameter to input a desired array
     */

    // Defining bubbleSort method
    public static void bubbleSort(int[] arr) {

        // Setting variable 'n' to the length of the array given
        int n = arr.length;

        // Defining our 'swapped' boolean
        boolean swapped;

        // Iterating through our array and swapping elements into the correct order
        for (int i = 0; i < n - 1; i++) {
            swapped = false;

            for (int j = 0; j < n - i - 1; j++) {

                if (arr[j] > arr[j + 1]) {
                    swapped = true;
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }

            // Returning the original array if nothing needed to be swapped
            if (!swapped) {

                return;
            }
        }
    }
}