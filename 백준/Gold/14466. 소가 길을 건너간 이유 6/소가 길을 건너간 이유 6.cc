#include <iostream>

class farm {
public:
    bool top, bottom, left, right, cow, visited;
    farm(bool top = true, bool bottom = true, bool left = true, bool right = true, bool cow = false, bool visited = false) {
        this->top = top;
        this->bottom = bottom;
        this->left = left;
        this->right = right;
        this->cow = cow;
        this->visited = visited;
    }
};

class cow {
public:
    bool check;
    int r, c;
    cow(int r = -1, int c = -1, bool check = false) {
        this->r = r;
        this->c = c;
        this->check = check;
    }
};

using namespace std;
const int LEN = 101;
int N, list[10000], wide[4][2] = { {1, 0},{-1,0}, {0, 1},{0, -1} };
farm farmMap[LEN][LEN];

void road(int r,int c,int rt,int ct) {
    if (rt == r + 1) {
        farmMap[r][c].right = false;
        farmMap[rt][ct].left = false;
    }
    else if (rt == r - 1) {
        farmMap[r][c].left = false;
        farmMap[rt][ct].right = false;
    }
    else if (ct == c + 1) {
        farmMap[r][c].top = false;
        farmMap[rt][ct].bottom = false;
    }
    else if (ct == c - 1) {
        farmMap[r][c].bottom = false;
        farmMap[rt][ct].top = false;
    }
}

int dfs(int r, int c) {
    int next_r, next_c, result = farmMap[r][c].cow ? 1:0;

    for (int i = 0; i < 4; i++) {
        next_r = r + wide[i][0];
        next_c = c + wide[i][1];

        if (next_r <= 0 || next_r > N || next_c <= 0 || next_c > N) continue; // 농장 밖

        if (farmMap[next_r][next_c].visited) continue;

        // 도로가 있다면 스킵
        if (i == 0 && !farmMap[r][c].right) continue;
        else if (i == 1 && !farmMap[r][c].left) continue;
        else if (i == 2 && !farmMap[r][c].top) continue;
        else if (i == 3 && !farmMap[r][c].bottom) continue;

        farmMap[next_r][next_c].visited = true;
        result += dfs(next_r, next_c);
    }
    return result;
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int K, R, r, c, rt, ct, idx = 0, result = 0;
    std::cin >> N >> K >> R;
    
    for (int i = 0; i < R; i++) {
        std::cin >> r >> c >> rt >> ct;
        road(r, c, rt, ct);
    }

    for (int i = 0; i < K; i++) {
        std::cin >> r >> c;
        farmMap[r][c].cow = true;
    }

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            if (farmMap[i][j].visited) continue;
            farmMap[i][j].visited = true;
            list[idx++] = dfs(i, j);
        }
    }

    for (int i = 0; i < idx; i++) {
        result += (K - list[i])* list[i];
        K -= list[i];
    }

    std::cout << result;
};