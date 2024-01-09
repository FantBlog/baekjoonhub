#include <iostream>

using namespace std;

const int LEN = 1001;
bool arr[LEN][LEN];
int n, m, total;

void start(int dy, int dx, int y, int x) {

	if (arr[y][x]) return;
	arr[y][x] = true;
	total--;
    
	if (y + dy < 1 || y + dy > n || x + dx < 1 || x + dx > m) return;

	start(dy, dx, dy + y, dx + x);
}

int main() {
	std::cin.tie(0)->sync_with_stdio(0);
	int Q, a, x, y, dx, dy;
	std::cin >> n >> m >> Q;

	total = n * m;

	for (int i = 0; i < Q; i++) {
		std::cin >> a;
		if (a == 1) {
			// dy, dx, y, x
			std::cin >> dy >> dx >> y >> x;
			start(dy, dx, y, x);
		}
		else if (a == 2) {
			std::cin >> y >> x;
			std::cout << arr[y][x] << "\n";
		}
		else {
			std::cout << total << "\n";
		}
	}
};