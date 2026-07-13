def solution(N, number):
    if N == number:
        return 1
    num = [set() for _ in range(9)]
    num[1].add(N)
    for i in range(2, 9):
        NNN = int(str(N) * i)
        for j in range(1, i):
            for a in num[j]:
                for b in num[i-j]:
                    if b == 0:
                        num[i].update([a + b, a - b, a * b, NNN])
                    else:
                        num[i].update([a + b, a - b, a * b, a // b, NNN])
        if number in num[i]:
            return i
    return -1