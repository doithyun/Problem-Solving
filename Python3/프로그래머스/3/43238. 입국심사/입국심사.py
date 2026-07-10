def solution(n, times):
    start = 1
    end = max(times) * n
    res = 0
    while(start <= end):
        mid = (start + end) // 2
        tmp = 0
        for t in times:
            tmp += (mid // t)
        if tmp >= n:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    return res