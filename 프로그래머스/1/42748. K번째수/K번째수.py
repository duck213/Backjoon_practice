def solution(array, commands):
    answer = []
    key = []
    for i in range (0, len(commands)):

        answer = array[commands[i][0]-1:commands[i][1]]
        answer.sort()
        third_num = commands[i][2]
        key.append(answer[third_num-1])

    return key