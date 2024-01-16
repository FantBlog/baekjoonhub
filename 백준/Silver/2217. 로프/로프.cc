#include <iostream>
#include <algorithm>

using namespace std;
const int LEN = 100001;
int rope[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int N, w;
    std::cin >> N;

    for (int i = 0; i < N; i++) {
        std::cin >> w;
        rope[i] = w;
    }

    sort(rope, rope + N, greater<int>());

    int result = 0;
    for (int i = 0; i < N; i++) {
        if (result < rope[i] * (i + 1)) result = rope[i] * (i + 1);
    }
    std::cout << result;
};