#include <iostream>

using namespace std;
const int LEN = 1'000'001;
int l[LEN];

int f(int a) {
    if (l[a] == a) return a;
    return l[a] = f(l[a]);
}
void mg(int a, int b) {
    a = f(a);
    b = f(b);
    if (a == b) return;
    l[a] = b;
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n, m, c, a, b;

    std::cin >> n >> m;

    for (int i = 0; i <= n; i++) l[i] = i;

    for (int i = 0; i < m; i++) {
        std::cin >> c >> a >> b;
        if (c == 0) mg(a, b);
        else {
            if (f(a) == f(b)) std::cout << "YES\n";
            else std::cout << "NO\n";
        }
    }
};