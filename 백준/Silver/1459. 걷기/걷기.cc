#include <iostream>

using namespace std;


int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int x, y, w, s, temp;
    long long result = 0;
    std::cin >> x >> y >> w >> s;

    if (x < y) {
        temp = x;
        x = y;
        y = temp;
    }

    if (s < 2 * w) {
        while (x > 0 && y > 0) {
            result += s;
            x--;
            y--;
        }

        while (x >= 2 && 2 * s < 2 * w) {
            result += 2 * s;
            x -= 2;
        }

        while (x > 0) {
            result += w;
            x--;
        }
    }
    else {
        while (y > 0) {
            result += w;
            y--;
        }

        while (x > 0) {
            result += w;
            x--;
        }
    }
    std::cout << result;
};