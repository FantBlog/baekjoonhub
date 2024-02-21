#include <iostream>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    int h, w, n, m, a, b;
    std::cin >> h >> w >> n >> m;
    n++;
    m++;
    a = h / n;
    a += h % n ? 1 : 0;
    b = w / m;
    b += w % m ? 1 : 0;

    std::cout << a * b;

};