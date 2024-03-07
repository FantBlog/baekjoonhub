#include <iostream>

using namespace std;

int m(int n){
    if(n < 40) return 40;
    return n;
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int a, b, c, d, e;
    std::cin >> a >> b >> c >> d >> e;
    std::cout << (m(a) + m(b) + m(c) + m(d) + m(e)) / 5;
};