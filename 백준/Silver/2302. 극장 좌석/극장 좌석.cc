#include <iostream>

using namespace std;
bool sit[41];
long long dp[41];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n, m, temp;
    std::cin >> n >> m;

    for (int i = 0; i < m; i++) {
        std::cin >> temp;
        sit[temp] = true;
    }

    dp[0] = 1;
    dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    long long count = 0, result = 1;
    for (int i = 1; i <= n; i++) {
        if (sit[i] == true) {
            result = result * dp[count];
            count = 0;
        }
        else count++;
    }
    result = result * dp[count];

    std::cout << result;
};