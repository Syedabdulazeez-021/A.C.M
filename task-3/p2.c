#include <stdio.h>
int main() {
    int a = 0, b = 1, c;
    int sum = 0;
    while (1) {
        c = a + b;
        a = b;
        b = c;
        printf("%d\n", c);
        if (c % 2 == 0) {
            sum += c;
        }
        if (c >= 4000000) {
            break;
        }
    }
    printf("Sum of even Fibonacci numbers less than 4000000 is %d\n", sum);
    return (0);
}
