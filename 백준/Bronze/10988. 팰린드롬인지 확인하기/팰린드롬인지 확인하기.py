n = list(input())
l = len(n)
rev = list(reversed(n))
if n[:l//2]==rev[:l//2]:
    print("1")
else:
    print("0")