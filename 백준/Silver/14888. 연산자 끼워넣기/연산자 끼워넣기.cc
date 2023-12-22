#include <iostream>

int l[11], op[4], N, max = -1e9, min = 1e9;

void f(int d, int sum) {
    if (d == N) {
        if (sum > max) max = sum;
        if (sum < min) min = sum;
        return;
    }
    int next;
    for (int i = 0; i < 4; i++) {
        if (op[i] == 0) continue;

        switch (i) {
            case 0:
                next = sum + l[d];
                break;
            case 1:
                next = sum - l[d];
                break;
            case 2:
                next = sum * l[d];
                break;
            case 3:
                next = sum / l[d];
                break;
        }

        op[i]--;
        f(d + 1, next);
        op[i]++;
    }

}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    std::cin >> N;

    for (int i = 0; i < N; i++) std::cin >> l[i];
    for (int i = 0; i < 4; i++) std::cin >> op[i];

    f(1, l[0]);
    
    std::cout << max << "\n" << min;
};