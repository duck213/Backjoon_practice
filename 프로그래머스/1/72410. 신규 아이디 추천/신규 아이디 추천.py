import re
def solution(new_id):
    answer = ''
    tmp_list = re.findall('[a-zA-Z0-9-_.]',new_id.lower())
    answer = ''.join(tmp_list)
    while ".." in answer:
        answer = answer.replace("..",".")
    if len(answer) > 0 and answer[0] == ".":
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == ".":
        answer = answer[:-1]
    if len(answer) == 0:
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    if len(answer) <= 3:
        answer = answer + answer[-1]*(3 - len(answer))
    return answer