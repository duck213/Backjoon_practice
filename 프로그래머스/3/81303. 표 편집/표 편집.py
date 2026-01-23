def solution(n, k, cmd):
    answer = ['O']*n
    bucket = []
    k += 1
    prev = [i-1 for i in range(n+2)]
    next2 = [i+1 for i in range(n+1)]


    for c in cmd:
        if c.startswith("C"):
            bucket.append(k)
            prev[next2[k]] = prev[k]
            next2[prev[k]] = next2[k]

            k = prev[k] if n < next2[k] else next2[k]


        elif c.startswith("Z"):
            rev = bucket.pop()
            next2[prev[rev]] = rev
            prev[next2[rev]] = rev

        else:
            move, num = c.split()
            if move == "U":
                for i in range(int(num)):
                    k = prev[k]
            else:
                for i in range(int(num)):
                    k = next2[k]

    for p in bucket:
        answer[p-1] = "X"

    return "".join(answer)
