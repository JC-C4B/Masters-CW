// Importing the 'Scanner' class so we can get user input for the factorial function
import java.util.Scanner;

// Definging our class where we keep all the functional code
public class A1 {

    // Defining our main method, similar to main function in Python
    public static void main(String[] args) {

        // Calling the factorial function within our main function
        fact();
    }

    // Defining our Factorial function
    public static void fact() {

        // Getting user input, and storing it in the variable 'n'
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please enter a positive integer: ");
        int n = scanner.nextInt();

        // Case if 'n' is negative
        while (n < 0) {
            System.out.print("Sorry, only positive numbers, try again: ");
            n = scanner.nextInt();
        }

        // Case if 'n' is 0
        if (n == 0) {
            System.out.println("The Factorial of 0 is 1");
        

        // Solving for the factorial of 'n' if it doesn't trigger any other cases
        } else {
            int f = 1;
            for (int i = 1; i <= n; i++) {
                f *= i;
            }

            // Printing the result of the factorial of 'n'
            System.out.println("The factorial of " + n + " is " + f);
        }

        // Closing scanner to resolve the 'resource leak' warning I got before
        scanner.close();

    }

}

