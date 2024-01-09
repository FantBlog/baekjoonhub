#include <iostream>

using namespace std;

const int LEN = 318137;
int superPrime[3001];

void Eratos()
{

	bool* PrimeArray = new bool[LEN + 1];

	for(int i= 0; i < 2; i++) PrimeArray[i] = false;
	for (int i = 2; i <= LEN; i++) PrimeArray[i] = true;

	for (int i = 2; i * i <= LEN; i++)
	{
		if (PrimeArray[i])
		{
			for (int j = i * i; j <= LEN; j += i)
				PrimeArray[j] = false;
		}
	}

	int count = 1, idx = 1;
	for (int i = 2; i <= LEN; i++)
	{
		if (PrimeArray[i]) {
			if (PrimeArray[count]) superPrime[idx++] = i;
			count++;
		}
	}
}
int main() {
    std::cin.tie(0)->sync_with_stdio(0);
    int T, n;
    std::cin >> T;

	Eratos();

    for (int i = 0; i < T; i++) {
        std::cin >> n;
		std::cout << superPrime[n] << "\n";
    }
};