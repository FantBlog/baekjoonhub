#include <iostream>

using namespace std;
const int LEN = 1e6;
int list[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    int T, N, h;
    long long result;
    std::cin >> T;

    for (int t = 0; t < T; t++) {
        std::cin >> N;
        result = 0;
        for (int i = 0; i < N; i++) {
            std::cin >> list[i];
        }
        h = list[N - 1];
        for (int i = N - 2; i >= 0; i--) {
            if (list[i] < h) result += h - list[i];
            else if (list[i] > h) h = list[i];
        }

        std::cout << result << "\n";
    }
};