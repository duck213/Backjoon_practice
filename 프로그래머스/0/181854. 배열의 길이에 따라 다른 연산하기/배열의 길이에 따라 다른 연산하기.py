def solution(arr, n):
    answer = []
    l = len(arr)
    for i in range(len(arr)):
        if l%2==1:
            if i%2==0:
                arr[i] = n+arr[i]
        elif l%2==0:
            if i%2==1:
                arr[i] = n+arr[i]    
    return arr