#include <iostream>

using namespace std;
const int LEN = 1000;
int arr[LEN][2], dp[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::cin >> arr[i][0] >> arr[i][1];
    }
    int mx = 0;
    for (int i = 0; i < n; i++) {
        if (i + arr[i][0] > n) continue;
        for (int j = 0; j < i; j++) dp[i] = max(dp[j], dp[i]);
        dp[i + arr[i][0]] = max(dp[i + arr[i][0]], dp[i] + arr[i][1]);
        mx = max(mx, dp[i + arr[i][0]]);
    }
    std::cout << mx;
};