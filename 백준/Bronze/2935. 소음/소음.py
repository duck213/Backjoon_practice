import operator
a = int(input())
o = input()
b = int(input())
ops = {"+":operator.add,"*":operator.mul}

print(ops[o](a,b))