#include <iostream>

using namespace std;

const int LEN = 41;
int a[LEN], b[LEN];

int fib(int n) {
    if (n == 1 || n == 2) return 1;
    else return (fib(n - 1) + fib(n - 2));
}

int fibonacci(int n) {
    b[1] = 1;
    b[2] = 1;
    b[3] = 1;

    for (int i = 4; i <= n; i++) b[i] = b[i - 1] + 1;

    return b[n];
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int N;
    std::cin >> N;

    std::cout << fib(N) << " " << fibonacci(N);
};