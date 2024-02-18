#include <iostream>
#include <algorithm>

using namespace std;
const int LEN = 10'001;

int list[LEN], arr[LEN];

int hap(int a, int b, int c, int d) {
    return a * 1000 + b * 100 + c * 10 + d;
}

int min_clock(int a, int b, int c, int d) {
    int h1, h2, h3, h4, result;
    h1 = hap(a, b, c, d);
    h2 = hap(b, c, d, a);
    h3 = hap(c, d, a, b);
    h4 = hap(d, a, b, c);
    result = min(h1, h2);
    result = min(result, h3);
    result = min(result, h4);
    return result;
}

int clock(int n) {
    int a, b, c, d;
    a = n % 10;
    n = n / 10;
    b = n % 10;
    n = n / 10;
    c = n % 10;
    n = n / 10;
    d = n;

    return min_clock(a, b, c, d);
}

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    for (int i = 1111; i < 10000; i++) {
        list[clock(i)]++;
    }
    int count = 0;
    for (int i = 1111; i < 10000; i++) {
        if (list[i] > 0) arr[count++] = i;
    }
    sort(arr, arr + count);

    int a, b, c, d, num;
    std::cin >> a >> b >> c >> d;
    num = min_clock(a, b, c, d);
    
    for (int i = 0; i < count; i++) {
        if (arr[i] == num) {
            std::cout << i + 1;
            break;
        }
    }
};