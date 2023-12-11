#include <iostream>

using namespace std;

const int LEN = 1000;
int input[LEN], a[LEN], b[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int N, now, start, end, mid, point = 0, b_point = 0, b_now, result = 0;
    std::cin >> N;
    for (int i = 0; i < N; i++) {
        std::cin >> input[i];
    }

    for (int i = 0; i < N; i++) {
        now = input[i];

        if (a[point] < now) {
            a[++point] = now;

            // 최고점 부터 감소하는 부분 수열 탐색? N ^ 2 풀이;;
            b[0] = now;
            b_point = 0;
            for (int j = i + 1; j < N; j++) {
                b_now = input[j];
                if (b[b_point] > b_now) b[++b_point] = b_now;
                else {
                    // 이분 탐색으로 지금꺼를 사이에 삽입
                    start = 0;
                    end = b_point;
                    while (start != end) {
                        mid = (start + end) / 2;
                        if (b[mid] > b_now) {
                            start = mid + 1;
                        }
                        else {
                            end = mid;
                        }
                    }
                    b[end] = b_now;
                }
            }
        }
        else {
            // 이분 탐색으로 지금꺼를 사이에 삽입
            start = 0;
            end = point;
            while (start != end) {
                mid = (start + end) / 2;
                if (a[mid] < now) {
                    start = mid + 1;
                }
                else {
                    end = mid;
                }
            }
            a[end] = now;
        }
        if (result < point + b_point) result = point + b_point;
    }
    std::cout << result;
};