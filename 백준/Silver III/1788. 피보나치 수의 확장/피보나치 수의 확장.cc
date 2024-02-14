#include <iostream>

using namespace std;
const int DIV = 1'000'000'000, A = 1'000'000;
int fibo[2'000'001];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    fibo[0 + A] = 0;
    fibo[1 + A] = 1;

    for (int i = -1; i >= -1'000'000; i--) {
        fibo[i + A] = (fibo[i + A + 2] - fibo[i + A + 1]) % DIV;
    }
    for (int i = 2; i <= 1'000'000; i++) {
        fibo[i + A] = (fibo[i + A - 2] + fibo[i + A - 1]) % DIV;
    }

    int temp;
    std::cin >> temp;
    int result1 = 0, result2 = 0;
    if (fibo[temp + A] > 0) {
        result1 = 1;
        result2 = fibo[temp + A];
    }
    else if (fibo[temp + A] < 0) {
        result1 = -1;
        result2 = -fibo[temp + A];
    }
    std::cout << result1 << "\n" << result2;
};