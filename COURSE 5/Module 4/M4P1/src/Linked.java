import java.util.LinkedList;
import java.util.Scanner;
import java.util.ListIterator;

/**
 * Simple class to create a Linked list from user input
 * that is sorted from smallest to largest.
 * 
 * @author Juan Carlos Cabrera
 * @version 1.0.0
 * @since Week 4 of CSC6301
 */

// Defining our main class
public class Linked {

    /** 
     * The main method of our class
     * @param args The default parameter for a main method - not used
     * @since Week 4 of CSC6301
     */

    // Defining our main method
    public static void main(String[] args) {

        // Creating the new scanner for user input
        Scanner sc = new Scanner(System.in);

        // Creating the Linked List 'linky' for storage
        LinkedList<Integer> linky = new LinkedList<Integer>();

        // Asking for user input
        System.out.print("Please enter the next number you'd like to add (0 for list/quit)");
        // Saving the input as a variable 'num'
        int num = sc.nextInt();

        // Allowing the user to input numbers until they enter 0
        while (num != 0){  

            // Adding the user input to the list
            inOrder(linky, num);
            System.out.print("Please enter the next number you'd like to add (0 for list/quit)");
            num = sc.nextInt();

        }
        
        // Printing out the sorted list
        System.out.println("Sorted Linked List: ");
        for (Integer number : linky) {
            System.out.print(number + " ");

        }

            // Closing the scanner
            sc.close();  

        }

        
        /** 
         * Method used to insert inputted integers into a linked list in ascending order
         * @param list Parameter to insert the Linked List you desire to be organized
         * @param num Parameter for the Integer being inserted
         * @since Week 4 of CSC6301
         */

        // Defining a method for the LinkedList Iterator
        public static void inOrder(LinkedList<Integer> list, int num) {
            
            // Creating the iterator
            ListIterator<Integer> it = list.listIterator();

            // Case if there is an element after the inserted element
            while (it.hasNext()) {

                // Setting the next element as a variable
                int next = it.next();

                // If the next element's value is >=, 
                // go to the element before it and insert there
                if (next >= num) {
                    it.previous();
                    it.add(num);
                    return;
                }
            }

            // If the integer is larger than everything in the list, 
            // we add it to the end.
            it.add(num);

            }
        }

