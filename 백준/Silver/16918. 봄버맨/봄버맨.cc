#include <iostream>

using namespace std;
int dir[4][2] = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };
int map[200][200];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int r, c, n;
    std::cin >> r >> c >> n;

    char temp;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            std::cin >> temp;
            if (temp == 'O') map[i][j] = 2;
        }
    }
    
    for (int t = 1; t < n; t++) {
        if (t % 2 == 1) {
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    if (map[i][j] == 0) map[i][j] = 3;
                    else map[i][j]--;
                }
            }
        }
        else {
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    if (map[i][j] == 1) {
                        for (int d = 0; d < 4; d++) {
                            int ni = i + dir[d][0], nj = j + dir[d][1];
                            if (ni < 0 || r <= ni) continue;
                            if (nj < 0 || c <= nj) continue;
                            if (map[ni][nj] > 1) map[ni][nj] = 0;
                        }
                        map[i][j] = 0;
                    }
                    else if (map[i][j] > 1) map[i][j]--;
                }
            }
        }
    }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (map[i][j] > 0) std::cout << 'O';
            else std::cout << '.';
        }
        std::cout << "\n";
    }
};