def solution(today, terms, privacies):
    answer = []
    dicted = {}
    yr, mo, da = 0,0,0
    for i in terms:
        a,b = i.split(" ")
        dicted[a] = int(b)
    for i, item in enumerate(privacies,1):
        date, term = item.split(" ")
        year, month, day = map(int,date.split("."))
        term = dicted[term]
        if month+term > 12:
            if (month+term) % 12 == 0:
                yr = (year + (month+term)//12) - 1
                mo = 12
            else:
                yr = year + (month+term)//12
                mo = (month + term) % 12
            da = day
        elif month+term <= 12:
            yr,mo,da = year,month+term,day
        if day == 1:
            da = 28
            if mo-1==0:
                mo = 12
                yr-=1
            else:
                mo-=1
        else:
            yr, mo, da = yr, mo, da-1     
        validated = str(yr)+"."+str(mo).zfill(2)+"."+str(da).zfill(2)
        if today > validated:
            answer.append(i)
    return answer