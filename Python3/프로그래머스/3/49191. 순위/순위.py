def solution(n, results):
    answer = 0
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for x, y in results:
        graph[x][y] = 1
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if graph[i][j] or graph[j][i] and i != j:
                cnt += 1
        if cnt == n - 1:
            answer += 1
    return answer