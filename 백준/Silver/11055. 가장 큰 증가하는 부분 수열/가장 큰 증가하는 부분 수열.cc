#include <iostream>

using namespace std;
const int LEN = 1000;
int arr[LEN], dp[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++) std::cin >> arr[i];
    
    dp[0] = arr[0];
    int mx = dp[0];
    for (int i = 1; i < n; i++) {
        dp[i] = arr[i];
        for (int j = 0; j < i; j++) {
            if (arr[j] >= arr[i]) continue;
            dp[i] = max(dp[i], dp[j] + arr[i]);
        }
        mx = max(mx, dp[i]);
    }
    std::cout << mx;
};