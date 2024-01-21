#include <iostream>

using namespace std;
const int LEN = 100;
int level[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n, result = 0;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::cin >> level[i];
    }

    for (int i = n - 1; i > 0; i--) {
        if (level[i - 1] >= level[i]) {
            result += level[i - 1] - level[i] + 1;
            level[i - 1] = level[i] - 1;
        }
    }
    std::cout << result;
};