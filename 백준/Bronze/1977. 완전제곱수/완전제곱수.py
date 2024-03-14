import math

a = int(input())
b = int(input())
list = []
summed = 0
for i in range(a, b+1):
    if math.sqrt(i).is_integer():
        list.append(i)
        summed += i

if not list:
    print('-1')
else:
    print(sum(list))
    print(min(list))