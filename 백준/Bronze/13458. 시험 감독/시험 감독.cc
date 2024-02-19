#include <iostream>

using namespace std;
const int LEN = 1'000'001;
int list[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n, b, c;
    std::cin >> n;

    for (int i = 0; i < n; i++) std::cin >> list[i];

    std::cin >> b >> c;

    long long result = 0;
    for (int i = 0; i < n; i++) {
        list[i] -= b;
        result++;
        if (list[i] <= 0) continue;
        result += list[i] / c;
        result += list[i] % c ? 1 : 0;
    }

    std::cout << result;
};