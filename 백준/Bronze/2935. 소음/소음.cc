#include <iostream>
#include <vector>

using namespace std;
const int LEN = 201;
int num[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    string a, b, c;
    std::cin >> a >> b >> c;

    if (b == "+") {
        num[a.length() - 1]++;
        num[c.length() - 1]++;
        if (a.length() > c.length()) {
            for (int i = a.length() - 1; i >= 0; i--) {
                std::cout << num[i];
            }
        }
        else{
            for (int i = c.length() - 1; i >= 0; i--) {
                std::cout << num[i];
            }
        }
    }
    else if (b == "*") {
        int temp;
        temp = (a.length() - 1) + (c.length() - 1);
        num[temp]++;
        for (int i = temp; i >= 0; i--) {
            std::cout << num[i];
        }
    }

};