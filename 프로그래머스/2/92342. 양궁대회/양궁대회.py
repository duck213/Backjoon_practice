def solution(n,info):
    global best_diff, best_answer
    best_diff = 0  
    best_answer = [-1]  
    
    def calc_score(ryan_info):
        ryan, apeach = 0, 0
        for i in range(11):
            if ryan_info[i] > info[i]:
                ryan += (10 - i)
            elif info[i] > 0:
                apeach += (10 - i)
        return ryan - apeach
    
    def is_better(new_info):
        for i in range(10, -1, -1):  
            if new_info[i] > best_answer[i]:
                return True
            elif new_info[i] < best_answer[i]:
                return False
        return False
    
    def dfs(score, arrows_left, ryan_info):
        global best_diff, best_answer
        
        if score < 0:
            ryan_info[10] += arrows_left
            diff = calc_score(ryan_info)
            
            if diff > 0: 
                if diff > best_diff:
                    best_diff = diff
                    best_answer = ryan_info[:]
                elif diff == best_diff and is_better(ryan_info):
                    best_answer = ryan_info[:]
            
            ryan_info[10] -= arrows_left
            return
        
        needed = info[score] + 1
        if arrows_left >= needed:
            ryan_info[score] = needed
            dfs(score - 1, arrows_left - needed, ryan_info)
            ryan_info[score] = 0 
        
        dfs(score - 1, arrows_left, ryan_info)
    

    ryan_info = [0] * 11
    dfs(10, n, ryan_info)
    
    return best_answer
    