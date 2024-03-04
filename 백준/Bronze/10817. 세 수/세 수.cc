#include <iostream>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int a, b, c;
    std::cin >> a >> b >> c;
    if (a >= b && b >= c)std::cout << b;
    else if (a <= b && b <= c)std::cout << b;
    else if (b >= a && a >= c)std::cout << a;
    else if (b <= a && a <= c)std::cout << a;
    else std::cout << c;
};