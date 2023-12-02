#include <iostream>
#include <vector>

using namespace std;

const int LEN = 100'001;
int visited[LEN];
vector<int> g[LEN];

int DFS(int index) {

    for (int i = 0; i < g[index].size(); i++) {
        int next = g[index][i];

        if (visited[next] == 0) {
            visited[next] = 1;
            visited[index] += DFS(next);
        }
    }
    return visited[index];
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int N, R, Q, U, V;

    std::cin >> N >> R >> Q;

    N--;
    while (N--) {
        std::cin >> U >> V;

        g[U].push_back(V);
        g[V].push_back(U);
    }

    visited[R] = 1;
    DFS(R);
    
    for (int i = 0; i < LEN; i++) g[i].clear();

    while (Q--) {
        int query;
        std::cin >> query;
        std::cout << visited[query] << "\n";
    }
};