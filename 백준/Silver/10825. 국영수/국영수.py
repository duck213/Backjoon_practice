N = int(input())
grades = []
for i in range(N):
    grades.append(input().split())
grades.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in range(N):
    print(grades[i][0])