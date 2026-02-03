def solution(code):
    ret = ''
    idx = 0
    mode = 0 
    for idx,char in enumerate(code):
        if mode == 1:
            if code[idx]!="1" and idx%2==1:
                ret+=code[idx]
            elif code[idx]=="1":
                mode = 0
        elif mode == 0:
            if code[idx] != "1" and idx%2==0:
                ret+=code[idx]
            elif code[idx]=="1":
                mode = 1
    return "EMPTY" if not ret else ret