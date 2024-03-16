n = list(input())
answer = 0
croatian = ['c=','c-','d-','lj','nj','s=','z=']
while n:
    if len(n)>2 and "".join(n[0:3]) == 'dz=':
        del n[:3]
    elif len(n)>1 and "".join(n[0:2]) in croatian:
        del n[:2]
    else:
        n.pop(0)
    answer += 1
print(answer)