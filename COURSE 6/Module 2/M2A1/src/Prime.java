// Importing scanner to get user input
import java.util.Scanner;

/**@author Juan Carlos Cabrera
 * Resubmitted to incorporate name in remarks!
 */

// Defining our main class
public class Prime {

// Definining main method
    public static void main(String[] args) {

        // Creating new scanner variable for user input
        Scanner sc = new Scanner(System.in);

        // Creating a placeholder variable for the integer we get from the scanner
        int n;

        do {

            // Prompt user for input, place in 'n'
            System.out.print("Enter a positive number (0 or negative to exit): ");
            n = sc.nextInt();

            // Case if 'n' <= 0, stop the loop
            if (n <= 0)    break;

            // If 'n' is not <= 0, check whether it is prime or not
            if (isPrime(n)) System.out.println(n + " is a prime number.");
            else        System.out.println(n + " is not a prime number.");  

        } 
        
        // Looping the main method until broken
        while (true);

        // Closing the scanner 
        sc.close();

    }

    // Defining isPrime method, returning a boolean
    public static boolean isPrime(int n) {

        // Cases for whether 'n' is prime or not
        if (n <= 1)                            return false;
        if (n <= 3)                            return true;
        if (n % 2 == 0 || n % 3 == 0)          return false;

        for (int i = 5; i * i <= n; i += 6) {

            if (n % i == 0 || n % (i + 2) == 0) return false;
        }

        return true;
    }

}
