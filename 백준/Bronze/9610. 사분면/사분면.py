n = int(input())
dic = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0, "AXIS": 0}
for i in range(n):
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        dic["AXIS"] += 1
    elif a > 0 and b > 0:
        dic["Q1"] += 1
    elif a < 0 < b:
        dic["Q2"] += 1
    elif a < 0 and b < 0:
        dic["Q3"] += 1
    elif a > 0 > b:
        dic["Q4"] += 1

print("Q1:", dic["Q1"])
print("Q2:", dic["Q2"])
print("Q3:", dic["Q3"])
print("Q4:", dic["Q4"])
print("AXIS:", dic["AXIS"])