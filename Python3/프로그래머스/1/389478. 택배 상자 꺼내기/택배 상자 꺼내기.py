from math import ceil
def solution(n, w, num):
    answer = 0
    block = []
    iter = ceil(n/w)
    for i in range(1, iter + 1):
        line = []
        for j in range(w * (i - 1) + 1, w * i + 1):
            if j > n:
                line.append(0)
            else:
                line.append(j)
        if i % 2 == 0:
            line.reverse()
        block.append(line)
    for i in range(len(block)):
        for j in range(w):
            if block[i][j] == num:
                row, col = i, j
    if block[iter-1][col] == 0:
        return iter-1-row
    else:
        return iter-row