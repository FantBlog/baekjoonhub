#include <iostream>
#include <vector>
#include <queue>

using namespace std;
const int LEN = 32001;
int in[LEN];
vector<int> nxt[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n, m;
    std::cin >> n >> m;

    int a, b;
    for (int i = 0; i < m; i++) {
        std::cin >> a >> b;
        in[b]++;
        nxt[a].push_back(b);
    }

    queue<int> que;
    bool end;
    while (true) {
        end = true;
        for (int i = 1; i <= n; i++) {
            if (in[i] == 0) {
                in[i]--;
                que.push(i);
                end = false;
            }
        }
        while (!que.empty()) {
            int top = que.front();
            std::cout << top << " ";
            for (int i = 0; i < nxt[top].size(); i++) {
                in[nxt[top][i]]--;
            }
            que.pop();
        }
        if (end) break;
    }
};