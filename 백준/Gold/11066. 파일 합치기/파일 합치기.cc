#include <iostream>
#include <algorithm>

using namespace std;
const int LEN = 501;
long long H[LEN], S[LEN], dp[LEN][LEN];


int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    S[0] = 0;
    int T, n;
    std::cin >> T;
    for (int t = 0; t < T; t++) {
        std::cin >> n;
        for (int i = 1; i <= n; i++) {
            std::cin >> H[i];
            S[i] = S[i - 1] + H[i];
        }

        for (int d = 1; d < n; d++) {
            for (int i = 1; i <= n - d; i++) {
                int j = i + d;
                dp[i][j] = 1e9;
                for (int m = i; m < j; m++) {
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j] + S[j] - S[i - 1]);
                }
            }
        }
        std::cout << dp[1][n] << "\n";
    }
};