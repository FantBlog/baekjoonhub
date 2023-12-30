#include <iostream>

using namespace std;
const int LEN = 1000;
int list[LEN], result[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n, count = 0, sec = 0;

    std::cin >> n;

    for (int i = 0; i < n; i++) std::cin >> list[i];

    int i = 0;
    while (count < n) {
        if (list[i] > 0) {
            list[i]--;
            sec++;

            if (list[i] == 0) {
                result[i] = sec;
                count++;
            }
        }

        i++;
        if (i == n) i = 0;
    }
    for (int i = 0; i < n; i++) std::cout << result[i] << " ";
};