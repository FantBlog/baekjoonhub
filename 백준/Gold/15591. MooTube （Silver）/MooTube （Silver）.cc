#include <iostream>
#include <vector>

class line {
public:
    int next;
    int value;
    line(int next, int value) {
        this->next = next;
        this->value = value;
    }
};

using namespace std;
const int LEN = 5'001;
int N, visited[LEN];
vector<line> g[LEN];

int dfs(int now,int usado, int p) {
    int result = usado < 1'000'000'001 ? 1 : 0;
    int next_usado;

    for (int i = 0; i < g[now].size(); i++) {
        if (visited[g[now][i].next] == 1) continue;

        visited[g[now][i].next] = 1;
        next_usado = usado > g[now][i].value ? g[now][i].value : usado;
        if (next_usado >= p) result += dfs(g[now][i].next, next_usado, p);
        visited[g[now][i].next] = 0;
    }
    return result;
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int Q;
    std::cin >> N >> Q;

    int p, q, r;
    for (int i = 1; i < N; i++) {
        std::cin >> p >> q >> r;
        g[p].push_back(line(q, r));
        g[q].push_back(line(p, r));
    }

    for (int i = 0; i < Q; i++) {
        std::cin >> p >> q;
        
        visited[q] = 1;
        std::cout << dfs(q, 1'000'000'001, p) << "\n";
        visited[q] = 0;
    }
};