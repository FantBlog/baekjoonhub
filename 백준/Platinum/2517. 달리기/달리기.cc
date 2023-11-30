#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>

using namespace std;

class cc {
public:
	int index, value, sorted_index;
};

const int LEN = 500'001;
int segTree[LEN * 4];
cc input_list[LEN], sorted_list[LEN];

cc cc_init(int index, int value) {
	cc result;
	result.index = index;
	result.value = value;
	return result;
}

bool compare(cc a, cc b) {
	return a.value < b.value;
}

void seg_input(int index, int start, int end, int value) {
	if (start == end) {
		segTree[index] = 1;
		return;
	}
	int mid = (start + end) / 2;

	if (value <= mid) seg_input(index * 2, start, mid, value);
	else seg_input(index * 2 + 1, mid + 1, end, value);

	segTree[index] = segTree[index * 2] + segTree[index * 2 + 1];
}

int seg_cnt(int index, int start, int end, int left, int right) {
	if (right < start || end < left) return 0;
	if (left <= start && end <= right) return segTree[index];

	int mid = (start + end) / 2;

	return seg_cnt(index * 2, start, mid, left, right) + seg_cnt(index * 2 + 1, mid + 1, end, left, right);
}

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	std::cin.tie(0)->sync_with_stdio(0);

	int N;
	std::cin >> N;

	for (int i = 1; i <= N; i++) {
		int value;
		std::cin >> value;
		input_list[i] = cc_init(i, value);
		sorted_list[i] = input_list[i];
	}

	sort(sorted_list + 1, sorted_list + N + 1, compare);

	for (int i = 1; i <= N; i++) {
		input_list[sorted_list[i].index].sorted_index = i;
	}
	/*
	for (int i = 1; i <= N; i++) {
		std::cout << input_list[i].value << ", " << input_list[i].index << ", " << input_list[i].sorted_index << "\n";
	}
	*/
	for (int i = 1; i <= N; i++) {
		seg_input(1, 1, N, input_list[i].sorted_index);
		// std::cout << input_list[i].sorted_index << ", " << seg_cnt(1, 1, N, input_list[i].sorted_index, N) << "\n";
		std::cout << seg_cnt(1, 1, N, input_list[i].sorted_index, N) << "\n";
	}
}