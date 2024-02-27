import re

def solution(s):
    string = ''
    temp = ''
    dic = ["zero","one","two","three","four",
           "five","six","seven","eight","nine"]
    for i in range(len(s)):
        temp += s[i]
        if temp.isdigit():
            string +=temp
            temp = ''
        elif temp in dic:
            string += str(dic.index(temp))
            temp=''
        
    answer = int(string) 
    return answer