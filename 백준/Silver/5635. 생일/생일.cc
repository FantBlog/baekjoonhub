#include <iostream>
#include <algorithm>

using namespace std;

class student {
public:
    string name;
    int dd, mm, yy;
    student(string name = "null", int dd = 0, int mm = 0, int yy = 0) {
        this->name = name;
        this->dd = dd;
        this->mm = mm;
        this->yy = yy;
    }
};

bool compare(student a, student b) {
    if (a.yy > b.yy) return true;
    else if (a.yy < b.yy) return false;

    if (a.mm > b.mm) return true;
    else if (a.mm < b.mm) return false;

    if (a.dd > b.dd) return true;
    else if (a.dd < b.dd) return false;
    
    return true;
}

const int LEN = 100;
student list[LEN];

int main() {
    std::cin.tie(0)->sync_with_stdio(0);

    int n;
    std::cin >> n;
    
    string name;
    int dd, mm, yy;
    for (int i = 0; i < n; i++) {
        std::cin >> name >> dd >> mm >> yy;
        list[i] = student(name, dd, mm, yy);
    }

    sort(list, list + n, compare);

    std::cout << list[0].name << "\n" << list[n - 1].name;
};