from sys import stdin
basket = []
for i in range(10):
    std = int(stdin.readline())
    if std%42 not in basket:
        basket.append(std%42)
print(len(basket))