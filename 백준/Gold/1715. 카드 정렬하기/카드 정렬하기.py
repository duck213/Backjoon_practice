import heapq as hq
N = int(input())
heap = []
for i in range(N):
    hq.heappush(heap, int(input()))
ans = 0
while len(heap)>1:
    a = hq.heappop(heap)
    b = hq.heappop(heap)
    ans += a+b
    hq.heappush(heap,a+b)
print(ans)