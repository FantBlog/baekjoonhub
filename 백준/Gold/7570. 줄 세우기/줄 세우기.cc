#include <iostream>

using namespace std;
const int LEN = 1'000'001;
int dp[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n, temp, result = 0;
    std::cin >> n;
    
    for (int i = 0; i < n; i++) {
        std::cin >> temp;
        dp[temp] = dp[temp - 1] + 1;
        if (dp[temp] > result) result = dp[temp];
    }

    std::cout << n - result;
};