#include <iostream>
#include <algorithm>

using namespace std;
const int LEN = 1e6 + 1, LEN2 = 1e3 + 1;
int List[LEN], ModList[LEN2];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n, m;
    std::cin >> n >> m;

    for (int i = 0; i < n; i++) {// 입력
        std::cin >> List[i]; 
        List[i] = List[i] % m;
    }

    ModList[List[0]]++;
    for (int i = 1; i < n; i++) {
        List[i] = (List[i - 1] + List[i]) % m;
        ModList[List[i]]++;
    }

    long long result = ModList[0], temp;
    for (int i = 0; i < m; i++) {
        temp = ModList[i];
        result += (temp * (temp - 1)) / 2;
    }

    std::cout << result;
};