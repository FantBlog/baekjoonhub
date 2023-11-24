#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<stdio.h>
#include<vector>
#include <cmath>

using namespace std;

class Node
{
public:
	int left = 0;
	int right = 0;
	int total = 0;
	int cnt = 0;

	Node() {}
	Node(int left, int right) : left(left), right(right) {}
	Node(int left, int right, int total, int cnt) : left(left), right(right), total(total), cnt(cnt) {}
	Node seg_copy()
	{
		return Node((*this).left, (*this).right, (*this).total, (*this).cnt);
	}
};

int head[300000 + 1];
int numbers[300000 + 1];
Node segTree[8000000];
int fac_list[300000 + 1];
long long MOD = 1000000007;

void seg_init(int idx, int node_st, int node_en) {
	if (node_st == node_en)
	{
		segTree[idx] = Node(0, 0);
		return;
	}
	int mid = (node_st + node_en) / 2;

	segTree[idx] = Node(idx * 2, idx * 2 + 1);

	seg_init(idx * 2, node_st, mid);

	seg_init(idx * 2 + 1, mid + 1, node_en);
}

int seg_input(int num, int idx, int fac, int left, int right)
{
	if (left == right) {
		segTree[idx].total = fac_list[fac];
		segTree[idx].cnt = 1;
		return 0;
	}

	int mid = (left + right) / 2;

	if (mid >= num)
	{
		segTree[idx + 1] = segTree[segTree[idx].left].seg_copy();
		segTree[idx].left = idx + 1;

		int under_count = seg_input(num, idx + 1, fac, left, mid);

		segTree[idx].total = (segTree[segTree[idx].left].total + segTree[segTree[idx].right].total) % MOD;
		segTree[idx].cnt = segTree[segTree[idx].left].cnt + segTree[segTree[idx].right].cnt;
		return under_count;
	}
	else
	{
		segTree[idx + 1] = segTree[segTree[idx].right].seg_copy();
		segTree[idx].right = idx + 1;

		int under_count = seg_input(num, idx + 1, fac, mid + 1, right);

		segTree[idx].total = (segTree[segTree[idx].left].total + segTree[segTree[idx].right].total) % MOD;
		segTree[idx].cnt = segTree[segTree[idx].left].cnt + segTree[segTree[idx].right].cnt;
		return under_count + segTree[segTree[idx].left].cnt;
	}
	return 0;
}

int get_seg_cnt(int start, int end, int idx, int left, int right)
{
	if (right < start || end < left) return 0;
	if (start <= left && right <= end) return segTree[idx].cnt;

	int mid = (left + right) / 2;

	return (get_seg_cnt(start, end, segTree[idx].left, left, mid) + get_seg_cnt(start, end, segTree[idx].right, mid + 1, right)) % MOD;
}


int get_seg_sum(int start, int end, int idx, int left, int right)
{
	if (right < start || end < left) return 0;
	if (start <= left && right <= end) return segTree[idx].total;

	int mid = (left + right) / 2;

	return (get_seg_sum(start, end, segTree[idx].left, left, mid) + get_seg_sum(start, end, segTree[idx].right, mid + 1, right)) % MOD;
}

int main()
{
	// 고속 입출력
	ios::sync_with_stdio(0);
	cin.tie(0);
	//

	int K, N;

	std::cin >> K >> N;

	// cal segTree size
	int maxRight = 0;
	int deep = 0;
	for (int i = 0; i < K; i++)
	{
		if (pow(2, i) >= K)
		{
			maxRight = (int)pow(2, i);
			deep = i + 1;
			break;
		}
	}

	// init factorial
	fac_list[0] = 1;
	for (long long i = 1; i <= K; i++) fac_list[i] = i * fac_list[i - 1] % MOD;

	// init seg tree
	segTree[0] = Node(0, 0);
	segTree[1] = Node(0, 0);
	seg_init(1, 1, maxRight);

	// init head seg tree
	head[0] = 1;
	head[1] = maxRight * 2;

	
	for (int i = 0; i < K; i++)
	{
		int input;
		cin >> input;
		numbers[i] = input;
	}

	long long input_result = 1;
	for (int i = 0; i < K; i++)
	{
		if (head[i + 1] == 0) head[i + 1] = head[i] + deep;

		segTree[head[i + 1]] = segTree[head[i]].seg_copy();

		long long under_count = seg_input(numbers[K - i - 1], head[i + 1], i, 1, maxRight);
		input_result = (input_result + under_count * fac_list[i] + MOD) % MOD;
	}

	for (int i = 0; i < N; i++)
	{
		int A, B;
		cin >> A >> B;

		int head_idx_a = head[K - A + 1];
		int head_idx_b = head[K - B + 1];

		long long result = input_result;

		if (numbers[A - 1] < numbers[B - 1])
		{
			int sm_number = numbers[A - 1];
			int lg_number = numbers[B - 1];

			result = (result - get_seg_cnt(sm_number + 1, lg_number - 1, head_idx_b, 1, maxRight) * fac_list[K - B] + MOD) % MOD;
			result = (result + get_seg_cnt(sm_number, lg_number - 1, head_idx_a, 1, maxRight) * fac_list[K - A] + MOD) % MOD;

			result = (result + get_seg_sum(sm_number + 1, lg_number - 1, head_idx_a, 1, maxRight) + MOD) % MOD;
			result = (result - get_seg_sum(sm_number + 1, lg_number - 1, head_idx_b, 1, maxRight) + MOD) % MOD;
		}
		else
		{
			int sm_number = numbers[B - 1];
			int lg_number = numbers[A - 1];

			result = (result + get_seg_cnt(sm_number + 1, lg_number - 1, head_idx_b, 1, maxRight) * fac_list[K - B] + MOD) % MOD;
			result = (result - get_seg_cnt(sm_number, lg_number - 1, head_idx_a, 1, maxRight) * fac_list[K - A] + MOD) % MOD;

			result = (result - get_seg_sum(sm_number + 1, lg_number - 1, head_idx_a, 1, maxRight) + MOD) % MOD;
			result = (result + get_seg_sum(sm_number + 1, lg_number - 1, head_idx_b, 1, maxRight) + MOD) % MOD;
		}
		std::cout << result << "\n";
	}
}
