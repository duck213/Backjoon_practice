def solution(my_strings, parts):
    answer = ''
    for k,item in zip(parts,my_strings):
        i,j = k
        answer+=item[i:j+1]
    return answer