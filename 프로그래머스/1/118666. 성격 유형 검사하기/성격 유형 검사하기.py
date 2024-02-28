def solution(survey, choices):
    answer = ''
    char = list("RTCFJMAN")
    char_dict = dict(zip(char,[0,0,0,0,0,0,0,0]))
    classed = ["RT","CF","JM","AN"]
    for i,j in enumerate(survey):
        if choices[i] > 4:
            char_dict[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            char_dict[survey[i][0]] += 4 - choices[i]
    for i in range(4):
        if char_dict[classed[i][0]]>=char_dict[classed[i][1]]:
            answer+=classed[i][0]
        else:
            answer+=classed[i][1]
    return answer
