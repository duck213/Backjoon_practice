#include <string>
#include <vector>
#include <numeric>
#include <iostream>

using namespace std;

double solution(vector<int> arr) {
    int acc = accumulate(arr.begin(), arr.end(), 0);
    return double(acc)/double(arr.size());
}