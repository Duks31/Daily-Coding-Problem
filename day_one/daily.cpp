// Write a function that takes a natural number as input and returns the number of digits the input has.
// Constraint: don't use any loops.

#include <string>
#include <iostream>

int number_of_digits(int n) {
    std::string str = std::to_string(n);
    return str.length();
}

int main() {
    std::cout << number_of_digits(1234) <<std::endl;
}
    