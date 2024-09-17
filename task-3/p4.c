#include <stdio.h>
int main() {
    long long sum = 0;
    for (int i = 2; i < 2000000; i++) {
        int is_prime = 1;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                is_prime = 0;
                break;
            }
        }
        if (is_prime) {
            sum += i;
        }
    }
    printf("The sum of all primes below 2000000 is %lld\n", sum);
    return (0);
}
