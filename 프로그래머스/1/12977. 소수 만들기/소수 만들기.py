def solution(nums):
    result = []
    summed = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                summed.append(nums[i]+nums[j]+nums[k])
    for l in summed:
        if all(l % m != 0 for m in range(2, l)):
            result.append(l)     
    return len(result)
