#include <iostream>

using namespace std;

const int LEN = 101;
int list[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int N, M, a, b, temp;

    std::cin >> N >> M;

    for (int i = 1; i <= N; i++) {
        list[i] = i;
    }

    for (int i = 0; i < M; i++) {
        std::cin >> a >> b;

        while (a < b) {
            temp = list[a];
            list[a] = list[b];
            list[b] = temp;
            a++;
            b--;
        }
    }

    for (int i = 1; i <= N; i++) {
        std::cout << list[i] << " ";
    }
};