#include <iostream>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int a, b, c, d, e, f;
    std::cin >> a >> b >> c >> d >> e >> f;

    for (int x = -999; x <= 999; x++) {
        for (int y = -999; y <= 999; y++) {
            if (a * x + b * y == c && d * x + e * y == f) {
                std::cout << x << " " << y;
                return 0;
            }
        }
    }

};