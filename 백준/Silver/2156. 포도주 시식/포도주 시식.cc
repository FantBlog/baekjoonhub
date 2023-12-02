#include <iostream>

using namespace std;

const int LEN = 10'001;
int input_list[LEN], DP[3][LEN];

int max(int a, int b) {
    if (a >= b) return a;
    return b;
}

int max(int a, int b, int c) {
    if (a >= b && a >= c) return a;
    else if (b >= a && b >= c) return b;
    return c;
}

int main() {
    int N, conti = 0;
    std::cin >> N;
    for (int i = 0; i < N; i++) std::cin >> input_list[i];

    DP[1][0] = input_list[0];

    for (int i = 0; i < N; i++) {
        DP[0][i + 1] = max(DP[0][i], DP[1][i], DP[2][i]);
        for (int j = 0; j < 2; j++) {
            DP[j + 1][i + 1] = max(DP[j][i] + input_list[i + 1], DP[j + 1][i]);
        }
    }

    std::cout << max(DP[0][N - 1], DP[1][N - 1], DP[2][N - 1]);
};