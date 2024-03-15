n = int(input())
stack = []
ink = []
for i in range(n):
    a = input()
    if a[:4]=='push':
        p,x = a.split()
        stack.append(int(x))
    elif a=='pop':
        if stack:
            z = stack.pop()
            ink.append(z)
        else:
            ink.append('-1')
    elif a=='size':
        ink.append(len(stack))
    elif a=='empty':
        ink.append('0') if stack else ink.append('1')
    elif a=='top':
        ink.append(stack[-1]) if stack else ink.append('-1')
for j in ink:
    print(j)