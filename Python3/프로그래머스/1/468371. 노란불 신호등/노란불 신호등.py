def GCD(a, b):
    x, y = max(a, b), min(a, b)
    if x % y == 0:
        return y
    else:
        return GCD(y, x % y)
def LCD(a, b):
    gcd = GCD(a, b)
    return a * b // gcd

def solution(signals):
    time = []
    for x in signals:
        time.append(x[0] + x[1] + x[2])
    while len(time) > 1:
        a = time.pop()
        b = time.pop()
        time.append(LCD(a, b))
    time2 = [[False] * (time[0] + 1) for _ in range(len(signals))]
    for i in range(len(signals)):
        term = sum(signals[i])
        for j in range(1, time[0] + 1):
            if signals[i][0] < j % term <= signals[i][0] + signals[i][1]:
                time2[i][j] = True
            
    for j in range(1, time[0] + 1):
        check = time2[0][j]
        for i in range(1, len(signals)):
            check = check and time2[i][j]
        if check:
            return j
    return -1