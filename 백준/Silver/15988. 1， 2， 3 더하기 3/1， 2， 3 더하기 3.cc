#include <iostream>

using namespace std;
const int LEN = 1'000'001, DIV = 1'000'000'009;
int dp[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    int n, now;
    std::cin >> n;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;

    for (int i = 4; i < LEN; i++) {
        dp[i] = ((dp[i - 1] + dp[i - 2]) % DIV + dp[i - 3]) % DIV;
    }
    
    for (int i = 0; i < n; i++) {
        std::cin >> now;
        std::cout << dp[now] << "\n";
    }
};