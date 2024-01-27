#include <iostream>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    int n;
    std::cin >> n;
    for(int i = n; i > 0; i--){
        for(int j = 0; j < i; j++){
            std::cout << "*";
        }
        std::cout << "\n";
    }
};