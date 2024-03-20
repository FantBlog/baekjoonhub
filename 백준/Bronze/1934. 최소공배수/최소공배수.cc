#include <iostream>

using namespace std;

int gcd(long long a, long long b) {
    int d;
    if (b > a) {
        d = b % a;
        if (d == 0) return a;
        return gcd(a, d);
    }
    d = a % b;
    if (d == 0) return b;
    return gcd(b, d);
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int t, c;
    long long a, b, result;
    std::cin >> t;
    while(t--) {
        std::cin >> a >> b;
        c = gcd(a, b);
        result = (a * b) / c;
        std::cout << result << "\n";
    }
};