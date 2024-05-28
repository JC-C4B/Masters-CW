// (Changed the imports to support a stack)
import java.util.Stack;
import java.util.Scanner;


/**
 * Simple class to create a Stack from user input
 * that is sorted from smallest to largest.
 * 
 * @author Juan Carlos Cabrera
 * @version 1.0.0
 * @since Week 5 of CSC6301
 */

// Defining our main class
public class Stacked {

    /** 
     * The main method of our class
     * @param args The default parameter for a main method - not used
     * @since Week 5 of CSC6301
     */

    // Defining our main method
    public static void main(String[] args) {

        // Creating the new scanner for user input
        Scanner sc = new Scanner(System.in);

        // Creating the Stack 'stacky' for storage
        // (Changed the Linked list to a stack)
        Stack<Integer> stacky = new Stack<Integer>();

        // Asking for user input
        System.out.print("Please enter the number you'd like to add (0 for stack/quit)");

        // Saving the input as a variable 'num'
        int num = sc.nextInt();

        // Allowing the user to input numbers until they enter 0
        while (num != 0){  

            // Adding the user input to the stack
            inOrder(stacky, num);
            System.out.print("Please enter the next number you'd like to add (0 for stack/quit)");
            num = sc.nextInt();

        }
        
        // Printing out the sorted stack
        // (Changed the printing method to work with the stack)
        System.out.println("Sorted Stack: ");
        while (!stacky.empty()){
            System.out.print(stacky.pop() + " ");
        }

        // Closing the scanner
        sc.close(); 

    }

        
        /** 
         * Method used to insert inputted integers into a stack in ascending order
         * @param Stack Parameter to insert the Stack to be organized
         * @param num Parameter for the Integer being inserted
         * @since Week 5 of CSC6301
         */

        // Defining a method for the organization of the stack
        // (For some help on this I referred to a youtube video,
        //  linked in the Stack plan document)
        public static void inOrder(Stack<Integer> stack, int num) {
            
            // Creating a temporary stack to organize the main stack
            Stack<Integer> tempStack = new Stack<Integer>();

            // Putting the elements from the main stack into the temp
            // If they are greater than the current number being added
            while (!stack.empty() && stack.peek() < num) {
                tempStack.push(stack.pop());
            }

            // Adding the current number to the main stack
            stack.push(num);

            // Putting the rest of the numbers from the temp stack
            // back into the main stack
            while (!tempStack.empty()) {
                stack.push(tempStack.pop());

            }
        }
    }

