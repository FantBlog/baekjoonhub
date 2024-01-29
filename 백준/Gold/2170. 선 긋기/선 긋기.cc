#include <iostream>
#include <algorithm>

using namespace std;
const int LEN = 1'000'001;

class node {
public:
    int start, end;
    node(int start = 0, int end = 0) {
        this->start = start;
        this->end = end;
    }
};
bool comp(node a, node b) {
    if (a.start < b.start) return true;
    return false;
}
node list[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n, s, e, end = -1'000'000'001, result = 0;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::cin >> s >> e;
        list[i] = node(s, e);
    }

    sort(list, list + n, comp);

    for (int i = 0; i < n; i++) {
        if (list[i].start > end) {
            result += list[i].end - list[i].start;
            end = list[i].end;
        }
        else if (list[i].end > end){
            result += list[i].end - end;
            end = list[i].end;
        }
    }
    std::cout << result;
};