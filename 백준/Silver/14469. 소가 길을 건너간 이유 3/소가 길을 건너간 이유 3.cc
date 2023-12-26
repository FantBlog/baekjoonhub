#include <iostream>
#include <algorithm>

class cow {
public:
    int start;
    int time;
    cow(int start = 0, int time = 0) {
        this->start = start;
        this->time = time;
    }
};

bool compare(cow a, cow b) {
    return a.start < b.start;
}

using namespace std;
const int LEN = 101;
cow list[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int N;
    std::cin >> N;

    int p, q;
    for (int i = 0; i < N; i++) {
        std::cin >> p >> q;
        list[i] = cow(p, q);
    }
    sort(list, list + N, compare);

    int time = 0;
    for (int i = 0; i < N; i++) {
        if (list[i].start > time) time = list[i].start;

        time += list[i].time;
    }

    std::cout << time;
};