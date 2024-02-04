#include <iostream>

using namespace std;
const int LEN = 1'001;
int jadu[LEN], dp[LEN][31];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    
    int t, w, result = 0;
    std::cin >> t >> w;

    for (int i = 0; i < t; i++) {
        std::cin >> jadu[i];
    }

    for (int i = 0; i <= w; i++) {
        for (int j = 0; j < t; j++) {
            if (j > 0) dp[j][i] = dp[j - 1][i];
            if (j > 0 && i > 0) dp[j][i] = max(dp[j - 1][i], dp[j - 1][i - 1]);

            if (i % 2 == 0 && jadu[j] == 1) dp[j][i]++;
            if (i % 2 == 1 && jadu[j] == 2) dp[j][i]++;
            if (result < dp[j][i]) result = dp[j][i];
        }
    }
    std::cout << result;
};