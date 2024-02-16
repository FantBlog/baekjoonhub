#include <iostream>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    int a, b;
    std::cin >> a >> b;
    std::cout << a * (b - 1) + 1;
};