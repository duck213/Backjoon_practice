def solution(number, k):
    stack = []
    cnt = 0
    for i in number:
        while cnt<k and len(stack) > 0 and stack[-1] < i:
            stack.pop()
            cnt+=1
        stack.append(i)
    return "".join(stack[:len(stack)-(k-cnt)])