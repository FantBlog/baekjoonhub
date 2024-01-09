#include <iostream>

using namespace std;

const int LEN = 1e5 + 1, DIV = 1e9 + 7;
int n, m, total, node[LEN];
long long c[LEN];


int main() {
	std::cin.tie(0)->sync_with_stdio(0);
	
	std::cin >> n >> m;

	c[3] = 1;
	for (int i = 4;i < LEN; i++) {
		c[i] = ((c[i - 1] * i) / (i - 3)) % DIV;
	}

	int u, v;
	for (int i = 0; i < m; i++) {
		std::cin >> u >> v;
		node[u]++;
		node[v]++;
	}

	int result = 0;
	for (int i = 1; i <= n;i++) {
		result = (result + c[node[i]]) % DIV;
	}
	std::cout << result;
};