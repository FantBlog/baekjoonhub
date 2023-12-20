#include <iostream>

using namespace std;

const int LEN = 601;
int arr[LEN][LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int H, W, X, Y;

    std::cin >> H >> W >> X >> Y;

    for (int i = 0; i < H + X; i++) {
        for (int j = 0; j < W + Y; j++) {
            std::cin >> arr[i][j];
        }
    }

    for (int i = 0; i < H ; i++) {
        for (int j = 0; j < W; j++) {
            arr[i + X][j + Y] -= arr[i][j];
            std::cout << arr[i][j] << " ";
        }
        std::cout << "\n";
    }
};