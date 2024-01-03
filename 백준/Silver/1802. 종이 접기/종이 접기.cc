#include <iostream>

using namespace std;

string input;

bool fun(int start, int end) {
    if (start >= end) return true;

    int mid = (start + end) / 2;

    for (int i = start; i < mid; i++) if (input[i] == input[end - i]) return false;

    return fun(start, mid - 1) && fun(mid + 1, end);
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n;
    string result;

    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::cin >> input;

        if (fun(0, input.length() - 1)) result = "YES";
        else result = "NO";

        std::cout << result << "\n";
    }
};