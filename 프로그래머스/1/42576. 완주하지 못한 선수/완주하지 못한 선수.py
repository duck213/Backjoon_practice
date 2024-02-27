def solution(participant, completion):
    dicted = {}
    hashed = 0
            
    for part in participant:
        dicted[hash(part)]=part
        hashed+=hash(part)
            
    for comp in completion:
        hashed-=hash(comp)
    return dicted[hashed]
