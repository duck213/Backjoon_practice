import heapq as hq
def solution(operations):
    answer = []
    heap = []
    hq.heapify(heap)
    for i in operations:
        a,b = i.split(" ")
        if a=="I":
            hq.heappush(heap,int(b))
        elif a=="D" and b=="-1" and heap:
            hq.heappop(heap) 
        elif a=="D" and b=="1" and heap:
            heap.remove(hq.nlargest(1, heap)[0])
    heap.sort()
    return [heap[-1],heap[0]] if heap else [0, 0]


