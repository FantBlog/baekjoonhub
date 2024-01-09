#include <iostream>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    int T, n;
    std::cin >> T;

    for (int i = 0; i < T; i++) {
        std::cin >> n;
        if (n > 2) std::cout << "3\n";
        else std::cout << "1\n";
    }
};