#include <iostream>
#include <vector>
#include <string>

using namespace std;
const string im = "IMPOSSIBLE\n";
const int LEN = 501;
int rk[LEN], index[LEN], incnt[LEN], check[LEN];
bool result;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int T, n, m, a, b;
    std::cin >> T;

    string total = "";
    for (int t = 0; t < T; t++) {
        result = false;

        std::cin >> n;
        for (int i = 1; i <= n; i++) {
            std::cin >> rk[i];
            index[rk[i]] = i;
            if (i > 1) {
                incnt[rk[i]] += i - 1;
            }
        }

        std::cin >> m;
        for (int i = 0; i < m; i++) {
            std::cin >> a >> b;
            if (index[a] > index[b]) {
                incnt[a]--;
                incnt[b]++;
            }
            else {
                incnt[a]++;
                incnt[b]--;
            }
        }

        for (int i = 1; i <= n; i++) {
            if (incnt[i] < 0) {
                result = true;
                break;
            }
            check[incnt[i]]++;
            rk[incnt[i]] = i;
        }
        for (int i = 0; i < n; i++) {
            if (check[i] == 0 && result == 0) result = true;
        }

        if (result) {
            total += im;
        }
        else {
            for (int i = 0; i < n; i++) {
                total += to_string(rk[i]) + " ";
            }
            total += "\n";
        }

        for (int i = 0; i <= n; i++) {
            check[i] = 0;
            incnt[i] = 0;
            rk[i] = 0;
            index[i] = 0;
        }
    }
    std::cout << total;
};