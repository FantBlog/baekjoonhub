#include <iostream>

using namespace std;


int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n, result = 0, money[] = { 500, 100, 50, 10, 5, 1 };
    std::cin >> n;

    n = 1000 - n;

    for (int i = 0; i < 6; i++) {
        while (n >= money[i]) {
            result++;
            n = n - money[i];
        }
    }

    std::cout << result;
};