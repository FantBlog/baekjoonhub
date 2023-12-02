#include <iostream>

using namespace std;

int m(int a, int b) {
    return a > b ? a : b;
}

int main() {
    int N, n, b{}, d[4]{};

    std::cin >> N;

    for (int i = 0; i < N; i++) {
        std::cin >> n;
        if (i == 0) d[3] = n;
        else if (i == 1) d[3] = d[2] + n;
        else d[3] = m(d[2], m(d[1] + n, d[0] + b + n));

        b = n;
        d[0] = d[1];
        d[1] = d[2];
        d[2] = d[3];
    }
    std::cout << d[3];
};