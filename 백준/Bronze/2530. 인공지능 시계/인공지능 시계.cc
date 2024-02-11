#include <iostream>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int h, m, s, t;
    std::cin >> h >> m >> s >> t;
    h += t / (60 * 60);
    t = t % (60 * 60);
    m += t / 60;
    t = t % 60;
    s += t;

    if (s >= 60) {
        m += s / 60;
        s = s % 60;
    }

    if (m >= 60) {
        h += m / 60;
        m = m % 60;
    }
    if (h >= 24) h = h % 24;

    std::cout << h << " " << m << " " << s;
};