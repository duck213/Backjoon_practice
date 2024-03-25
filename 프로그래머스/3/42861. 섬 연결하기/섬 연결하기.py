def find(tree,v):
    if tree[v] != v:
        tree[v] = find(tree,tree[v])
    return tree[v]

def union(tree, v1, v2):
    r1 = find(tree, v1)
    r2 = find(tree, v2)
    if r1<r2:
        tree[r2] = r1
    else:
        tree[r1] = r2

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    node = []
    tree = {i:i for i in range(n)}
    
    for a,b,c in costs:
        if find(tree,a)!=find(tree,b):
            union(tree,a,b)
            answer+=c
    return answer