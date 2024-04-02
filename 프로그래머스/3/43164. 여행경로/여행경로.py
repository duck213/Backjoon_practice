def dfs(tickets, pas, visited, answer):
    if len(answer) == len(tickets) + 1:
        return
    tmp = []
    pt_point = {}
    for i, tick in enumerate(tickets):
        f, t = tick
        if f == pas[1]:
            pt_point[i] = t
    pt_point = sorted(pt_point.items(), key=lambda x: x[1])
    
    for k, v in pt_point:
        if not visited[k]:
            visited[k] = True
            answer.append(v)
            pas = tickets[k]
            dfs(tickets, pas, visited, answer)
            if len(answer) == len(tickets) + 1:
                break
            visited[k] = False
            answer.pop()

def solution(tickets):
    length = len(tickets)
    answer, visited = ["ICN"], [False] * length
    st_point = {}
    for i, tick in enumerate(tickets):
        f, t = tick
        if f == "ICN":
            st_point[i] = t
    st_point = sorted(st_point.items(), key=lambda x: x[1])
    for k, v in st_point:
        visited[k] = True
        answer.append(v)
        pas = ["ICN", v]
        dfs(tickets, pas, visited, answer)
        if len(answer) == len(tickets) + 1:
            break
        visited[k] = False
        answer.pop()
    return answer