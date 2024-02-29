#include <iostream>
#include <algorithm>

using namespace std;
const int LEN = 10000;
int one[LEN], cha[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n, k;
    std::cin >> n >> k;

    for (int i = 0; i < n;i++) std::cin >> one[i];

    sort(one, one + n);

    for (int i = 0; i < n - 1; i++) cha[i] = one[i + 1] - one[i];

    sort(cha, cha + n - 1);

    if (k >= n) {
        std::cout << 0;
    }
    else {
        long long result = 0;
        for (int i = 0; i < n - k; i++) {
            result += cha[i];
        }
        std::cout << result;
    }
};