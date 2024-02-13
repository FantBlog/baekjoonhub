#include <iostream>
#include <queue>

using namespace std;

class node {
public:
    int r, c;
    node(int r = 0, int c = 0) {
        this->r = r;
        this->c = c;
    }
};
struct state {
    int d;
    node r;
    node b;
    int t;
};

queue<state> q;
char board[20][20];
int n, m, dir[4][2] = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };
// 동 서 남 북

int bfs(int d, node r, node b, int t) {
    if (t > 10) return -1;

    node nr = r, nb = b;
    bool o, p;
    int end = 0;

    while (true) {
        o = false;
        p = false;

        if (nr.r != -1 && nr.c != -1) {
            // red move
            nr.r += dir[d][0];
            nr.c += dir[d][1];

            // exit
            if (nb.r == nr.r && nb.c == nr.c) {
                nr.r -= dir[d][0];
                nr.c -= dir[d][1];
                o = true;
            }
            else if (board[nr.r][nr.c] == 'O') {
                if (end != -1) end = t;
                nr.r = -1;
                nr.c = -1;
                o = true;
            }
            else if (board[nr.r][nr.c] == '#') {
                nr.r -= dir[d][0];
                nr.c -= dir[d][1];
                o = true;
            }
        }
        else o = true;

        if (nb.r != -1 && nb.c != -1) {
            // blue move
            nb.r += dir[d][0];
            nb.c += dir[d][1];

            // exit
            if (nb.r == nr.r && nb.c == nr.c) {
                nb.r -= dir[d][0];
                nb.c -= dir[d][1];
                p = true;
            }
            else if (board[nb.r][nb.c] == 'O') {
                end = -1;
                p = true;
                nb.r = -1;
                nb.c = -1;
            }
            else if (board[nb.r][nb.c] == '#') {
                nb.r -= dir[d][0];
                nb.c -= dir[d][1];
                p = true;
            }
        }
        else p = true;

        if (o && p) break;
    }


    if (end != 0) return end;

    if (t + 1 > 10) return -1;
    if (nr.r != r.r || nr.c != r.c || nb.r != b.r || nb.c != b.c) {
        for (int i = 0; i < 4; i++) if(i != d) q.push(state{ i, nr, nb, t + 1 });
    }
    return -1;
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    node r, b;
    std::cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            std::cin >> board[i][j];

            if (board[i][j] == 'R') {
                r = node(i, j);
                board[i][j] = '.';
            }
            else if (board[i][j] == 'B') { 
                b = node(i, j);
                board[i][j] = '.';
            }
        }
    }
    
    for (int i = 0; i < 4; i++) {
        q.push(state{i, r, b, 1});
    }

    int result = -1;
    while (!q.empty()) {
        state now = q.front();
        q.pop();

        result = bfs(now.d, now.r, now.b, now.t);

        if (result > 0) break;
    }

    std::cout << result;
};