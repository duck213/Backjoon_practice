def solution(s):
    answer = ''
    temp = ''
    string = s.split(" ")
    for i, num in enumerate(string):
        if num != "" and len(num) > 0:
            for j, word in enumerate(num):
                if j % 2 == 0:
                    temp += num[j].upper()
                elif j % 2 == 1:
                    temp += num[j].lower()
            string[i] = temp
        elif num == "":
            pass
        temp = ''
    return " ".join(string)