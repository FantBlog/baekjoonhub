#include <iostream>
#include <algorithm>

using namespace std;

const int LEN = 100001;
int list[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int N, x;
    std::cin >> N;

    for (int i = 0; i < N; i++) {
        std::cin >> list[i];
    }
    sort(list, list + N);
    std::cin >> x;

    int left = 0, right = N - 1, result = 0;

    while (1) {
        if (left >= right) break;

        if (list[left] + list[right] == x) {
            result++;
            left++;
            right--;
        }
        else if (list[left] + list[right] < x)left++;
        else right--;
    }
    std::cout << result;
};