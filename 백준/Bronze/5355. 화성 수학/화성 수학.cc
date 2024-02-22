#include <iostream>
#include <string>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    std::cout << fixed;
    std::cout.precision(2);

    int t;
    double num;
    string temp;

    std::cin >> t;
    std::cin >> num;

    for (int i = 0; i < t - 1; i++) {
        for (int j = 0; j < 4; j++) {
            std::cin >> temp;

            if (temp == "@") num = num * 3;
            else if (temp == "%") num = num + 5;
            else if (temp == "#") num = num - 7;
            else {
                std::cout << num << "\n";
                num = stod(temp);
                break;
            }
        }
    }
    while (std::cin >> temp) {
        if (temp == "@") num = num * 3;
        else if (temp == "%") num = num + 5;
        else if (temp == "#") num = num - 7;
    }
    std::cout << num;
};