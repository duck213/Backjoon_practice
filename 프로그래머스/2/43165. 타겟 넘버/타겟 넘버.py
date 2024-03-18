answer = 0
def dfs(depth,cnt,numbers,target):
    if depth==len(numbers) and cnt==target:
        global answer
        answer+=1
    elif depth<len(numbers):
        dfs(depth+1,cnt+numbers[depth],numbers,target)
        dfs(depth+1,cnt-numbers[depth],numbers,target)

def solution(numbers, target):
    dfs(0,0,numbers,target)
    return answer