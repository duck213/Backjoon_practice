def solution(s):
    zero_count = 0
    convert = 0
    while len(s) > 1:
        zero_count += s.count("0")
        s = s.replace('0','')
        s = format(len(s),'b')
        convert+=1

    return [convert, zero_count]