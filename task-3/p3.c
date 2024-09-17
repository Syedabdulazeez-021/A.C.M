#include <stdio.h>
int sumOfSquares() {
    int sum = 0;
    for (int i = 1; i <= 100; i++) {
        sum += i * i;
    }
    return sum;
}
int squareOfSum() {
    int sum = 0;
    int square = 0;
    for (int i = 1; i <= 100; i++) {
        sum += i;
    }
    square = sum * sum;
    return square;
}
int main() {
    int a = sumOfSquares();
    int b = squareOfSum();
    int c = b - a;
    printf("The required result is %d\n", c);
    return (0);
}
