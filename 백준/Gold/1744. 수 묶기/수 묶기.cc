#include <iostream>
#include <algorithm>

using namespace std;
const int LEN = 51;
long long a[LEN], b[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n, temp, o = 0, p = 0;
    long long result = 0;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::cin >> temp;
        if (temp > 0) a[o++] = temp;
        else b[p++] = temp;
    }

    sort(a, a + o, greater<int>());
    sort(b, b + p);

    for (int i = 0; i < o; i += 2) {
        if (i + 1 < o) {
            if(a[i] * a[i + 1] > a[i] + a[i + 1]) result += a[i] * a[i + 1];
            else result += a[i] + a[i + 1];
        }
        else result += a[i];
    }
    for (int i = 0; i < p; i += 2) {
        if (i + 1 < p) {
            if(b[i] * b[i + 1] > b[i] + b[i + 1]) result += b[i] * b[i + 1];
            else result += b[i] + b[i + 1];
        }
        else result += b[i];
    }

    std::cout << result;
};