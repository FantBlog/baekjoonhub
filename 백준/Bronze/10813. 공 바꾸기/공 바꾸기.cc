#include <iostream>
#include<stdio.h>
#include<vector>

using namespace std;
int main()
{
	// 고속 입출력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N, M, a, b, temp;
	
	std::cin >> N >> M;

	vector<int> v;
	for (int i = 0; i <= N; i++) v.push_back(i);

	for (int i = 0; i < M; i++)
	{
		std::cin >> a >> b;

		temp = v[a];
		v[a] = v[b];
		v[b] = temp;
	}
	for (int i = 1; i <= N; i++) std::cout << v[i] << " ";
}