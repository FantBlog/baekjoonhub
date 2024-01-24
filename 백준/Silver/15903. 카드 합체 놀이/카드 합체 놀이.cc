#include <iostream>
#include <queue>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    priority_queue<long long, vector<long long>, greater<long long>> pq;
    
    int n, m;
    
    long long a, b, result = 0;
    std::cin >> n >> m;

    for (int i = 0; i < n; i++) {
        std::cin >> a;
        pq.push(a);
        result += a;
    }

    for (int i = 0; i < m; i++) {
        a = pq.top();
        pq.pop();

        b = pq.top();
        pq.pop();

        result += a;
        result += b;

        pq.push(a + b);
        pq.push(a + b);
    }
    std::cout << result;
};