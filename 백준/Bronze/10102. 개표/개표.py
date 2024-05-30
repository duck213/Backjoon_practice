n = int(input())
v = input()
vote = list(v)
dic = {'A':0, 'B':0}
for i in vote:
    dic[i] += 1

if dic['A']>dic['B']:
    print("A")
elif dic['A']<dic['B']:
    print("B")
elif dic['A']==dic['B']:
    print("Tie")
