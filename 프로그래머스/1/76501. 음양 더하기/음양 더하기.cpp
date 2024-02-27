#include <string>
#include <vector>
#include <numeric>
using namespace std;

int solution(vector<int> absolutes, vector<bool> signs) {
    for(int i=0;i<signs.size();i++)
    {
        if(signs.at(i) == false)
            absolutes[i] *= -1;
    }
    int sum = accumulate(absolutes.begin(), absolutes.end(), 0);
    return sum;
}