// Importing scanner for user input
import java.util.Scanner;

// Defining public class
public class Square {
    // Defining main method
    public static void main(String[] args) {
        // Printing out welcoming statement and a space
        System.out.println("This program computes the square of an integer");
        System.out.println();

        // Asking for user input and storing it in variable 'n'
        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter an integer: ");
        int n = sc.nextInt();

        // Closing scanner to avoid issues
        sc.close();

        // Caclulating the square of 'n'
        int acc = 0;
        int odd = 1;
        for (int i = 0; i < n; i ++) {
            acc += odd;
            odd += 2;
        }

        // Printing the results of the square equation
        System.out.println("The square of " + n + " is " + acc);
    
    }
}
