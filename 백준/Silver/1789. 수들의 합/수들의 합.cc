#include <iostream>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    long long N, result = 0, i = 1;
    std::cin >> N;
    while (true){
        result += i++;
        if (result > N) {
            std::cout << i - 2;
            break;
        }
    }
};