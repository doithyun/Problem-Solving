from collections import deque
def solution(players, m, k):
    cnt = 0
    server = 0
    queue = deque()
    for i in range(len(players)):
        for j in range(len(queue)):
            queue[j] -= 1
        while queue and queue[0] == 0:
            queue.popleft()
            server -= 1
        if players[i] >= m * server + 1:
            count = players[i] // m - server
            for _ in range(count):
                queue.append(k)
            server += count
            cnt += count
    return cnt