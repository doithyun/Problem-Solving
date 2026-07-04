from collections import deque
def solution(n, computers):
    answer = 0
    queue = deque()
    visited = [False] * n
    for i in range(len(computers)):
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            answer += 1
            while(queue):
                x = queue.popleft()
                for idx, element in enumerate(computers[x]):
                    if not visited[idx] and element == 1:
                        queue.append(idx)
                        visited[idx] = True
    return answer