#include <iostream>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    string word;
    std::cin >> word;
    
    int i = 0, j = word.length() - 1, result = 1;
    while (i < j) {
        if (word[i] != word[j]) {
            result = 0;
            break;
        }
        i++;
        j--;
    }
    std::cout << result;
};