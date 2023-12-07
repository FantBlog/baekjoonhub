#include <iostream>

using namespace std;

const int LEN = 21;
int dp[LEN][LEN][LEN];

int w(int a, int b, int c) {
    if (a <= 0 || b <= 0 || c <= 0) return 1;
    
    
    if (a > 20 || b > 20 || c > 20) {
        if (dp[20][20][20] != 0) return dp[20][20][20];
        dp[20][20][20] = w(20, 20, 20);
        return dp[20][20][20];
    }

    if (dp[a][b][c] != 0) return dp[a][b][c];

    if (a < b && b < c) {
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
        return dp[a][b][c];
    }
    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
    return dp[a][b][c];
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    dp[0][0][0] = 1;

    int a, b, c;
    while (true) {
    std:;cin >> a >> b >> c;
        if (c == -1 && a == b && b == c) return 0;
        std::cout << "w(" << a << ", " << b <<", " << c << ") = " << w(a, b, c) << "\n";
    };
};