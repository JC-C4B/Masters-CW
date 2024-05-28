// Code Conversion by Juan Carlos Cabrera
// Creating the main package
package main

// Importing fmt
import "fmt"

// Defining the main function and calling the tribonacci function
func main() {
	// Calling for the first 20 numbers in the tribonacci sequence
	fmt.Println(tribonacci(20))
}

// Defining the tribonacci function
func tribonacci(n int) []int {
	// Cases for n <= 0, n = 1, and n = 2; recursively calling the function if otherwise
	if n <= 0 {
		return []int{}
	} else if n == 1 {
		return []int{0}
	} else if n == 2 {
		return []int{0, 1}
	} else {
		fs := []int{1, 1, 1}
		for i := 3; i < n; i++ {
			next := fs[i-1] + fs[i-2] + fs[i-3]
			fs = append(fs, next)
		}
		return fs
	}
}
