n = int(input())
score = list(map(int,input().split()))
m = max(score)
score_man = [i/m*100 for i in score]
print(sum(score_man)/n)
