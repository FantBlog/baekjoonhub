#include <iostream>

using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    string i;
    std::cin >> i;
    if(i == "A+") std::cout << "4.3";
    else if(i == "A0") std::cout << "4.0";
    else if(i == "A-") std::cout << "3.7";
    else if(i == "B+") std::cout << "3.3";
    else if(i == "B0") std::cout << "3.0";
    else if(i == "B-") std::cout << "2.7";
    else if(i == "C+") std::cout << "2.3";
    else if(i == "C0") std::cout << "2.0";
    else if(i == "C-") std::cout << "1.7";
    else if(i == "D+") std::cout << "1.3";
    else if(i == "D0") std::cout << "1.0";
    else if(i == "D-") std::cout << "0.7";
    else if(i == "F") std::cout << "0.0";
};