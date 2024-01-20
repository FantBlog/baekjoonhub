#include <iostream>

using namespace std;


int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    string n;
    int z = 0, o = 0, before = -1;
    std::cin >> n;

    for (int i = 0; i < n.length(); i++) {
        if (n[i] == '0' && before != '0') {
            z++;
        }
        else if(n[i] == '1' && before != '1') {
            o++;
        }
        before = int(n[i]);
    }
    std::cout << (z < o ? z : o);
};