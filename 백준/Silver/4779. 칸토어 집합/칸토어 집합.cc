#include <iostream>
#include <cmath>

using namespace std;

string kantor(int d){
    if (d == 0) return "-";
    string mid;
    for (int i = 0; i < (int)pow(3, d - 1); i++) mid += " ";
    return kantor(d - 1) + mid + kantor(d - 1);
};

int main(){
    int N;
    while(true){
        std::cin >> N;
        if(std::cin.eof()) break;
        std::cout << kantor(N) << "\n";
    }
};