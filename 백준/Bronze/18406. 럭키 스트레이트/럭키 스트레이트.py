N = input()
lis = list(map(int,N))
h_len = len(lis) // 2
if sum(lis[:h_len])==sum(lis[h_len:]):
    print("LUCKY")
else:
    print("READY")
