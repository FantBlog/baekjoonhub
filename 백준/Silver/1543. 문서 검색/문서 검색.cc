#include <iostream>
#include <string>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    string a, b;
    getline(cin, a);
    getline(cin, b);
    
    int result = 0;
    for (int i = 0; i < a.length(); i++) {
        if (a[i] == b[0]) {
            for (int j = 0; j < b.length();j++) {
                if (a[i + j] != b[j]) break;
                if (j == b.length() - 1) {
                    result++;
                    i = i + j;
                }
            }
        }
    }
    std::cout << result;
};