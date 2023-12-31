#include <iostream>

using namespace std;
const int LEN = 20;
int list[LEN][LEN], visited;

int fun(int deep, int n, int bit) {
    if (deep == 2) {
        int idx = 0, sg[2] = { 0, 0 };
        for (int i = 0; i < n; i++) {
            if (visited & 1 << i) sg[idx++] = i;
        }
        if (idx == 2) return list[sg[0]][sg[1]] + list[sg[1]][sg[0]];
        return 0;
    }

    int result = 0;
    for (int i = 0; i < n; i++) {
        if (visited & 1 << i) continue;

        if (bit & 1 << i) {
            visited |= 1 << i;
            result += fun(deep + 1, n, bit);
            visited &= ~(1 << i);
        }
    }
    return result;
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n;

    std::cin >> n;

    int max_bit = 1 << n - 1, bit, count, a, b, result = 101;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::cin >> list[i][j];
        }
    }

    for (bit = 0; bit < max_bit; bit++) {
        count = 0;
        for (int j = 0; j < n; j++) {
            if (bit & 1 << j) count++;
        }
        if (count != n / 2) continue;

        a = fun(0, n, bit);
        b = fun(0, n, ~bit);
        if (a >= b && result > a - b) result = a - b;
        else if (b > a && result > b - a) result = b - a;
    }
    std::cout << result / 2;
};