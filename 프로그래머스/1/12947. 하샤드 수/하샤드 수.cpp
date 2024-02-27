#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    string str = to_string(x);
    string conv = "";
    int rex = 0;
    
    for(int i=0; i<str.length(); i++)
    {
        conv = str[i];
        rex += stoi(conv);
    }
    if(x%rex!=0)
        answer = false;

    return answer;
}