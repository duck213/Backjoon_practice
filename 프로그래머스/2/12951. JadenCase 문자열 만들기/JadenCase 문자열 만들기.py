def solution(s):
    string = s.split(" ")
    for i,num in enumerate(string):
        if num != "" and len(num) > 0 and num[0].isalpha():
            string[i] = num[0].upper() + num[1:].lower()
        elif num != "" and num[0].isdigit():
            string[i] = num[0] + num[1:].lower()
        elif num == "":
            pass
        
    return " ".join(string)