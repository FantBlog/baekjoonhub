#include <iostream>

using namespace std;

class people {
public:
    int r, c;
    char o;
    people(int r = 0, int c = 0, char o = 'X') {
        this->r = r;
        this->c = c;
        this->o = o;
    }
};

const int LEN = 6;
int n, direc[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
short sel[3];
char sch[LEN][LEN];
people T[6], S[30], X[36];

bool dfs(int r, int c, int dir) { // 학생을 감시 했다면 True
    int next_r, next_c;
    next_r = r + direc[dir][0];
    next_c = c + direc[dir][1];

    if (next_r < 0 || next_r >= n || next_c < 0 || next_c >= n) return false;

    if (sch[next_r][next_c] == 'S') return true;
    if (sch[next_r][next_c] == 'O') return false;
    return dfs(next_r, next_c, dir);
}

bool check(int t) {
    for (int i = 0; i < 3; i++) { // 장애물 설치
        sch[X[sel[i]].r][X[sel[i]].c] = 'O';
    }

    bool result = true;
    for (int i = 0; i < t; i++) {
        for (int j = 0; j < 4; j++) {
            if (dfs(T[i].r, T[i].c, j)) { // 학생을 감시 했다면
                result = false;
                break;
            }
        }
    }

    for (int i = 0; i < 3; i++) { // 장애물 제거
        sch[X[sel[i]].r][X[sel[i]].c] = 'X';
    }

    return result;
}

bool select(int deep, int s, int e, int t) { // 장애물 3개 고르기
    if (deep == 3) {
        return check(t); // true라면 감지 X
    }

    for (int i = s; i < e; i++) {
        sel[deep] = i;
        if (select(deep + 1, i + 1, e, t)) return true;
    }
    return false;
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    std::cin >> n;
    
    int t = 0, s = 0, x = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::cin >> sch[i][j];

            if (sch[i][j] == 'T') T[t++] = people(i, j, 'T');
            else if (sch[i][j] == 'S') S[s++] = people(i, j, 'S');
            else X[x++] = people(i, j, 'X');
        }
    }

    string result = "NO";
    if (select(0, 0, x, t)) result = "YES";
    std::cout << result;
};