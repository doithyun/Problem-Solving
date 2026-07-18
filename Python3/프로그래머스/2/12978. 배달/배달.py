import heapq
INF = float('inf')
def solution(N, road, K):
    answer = 0
    pq = []
    distance = [INF] * (N + 1)
    distance[1] = 0
    heapq.heappush(pq, (0, 1))
    while pq:
        dist, node = heapq.heappop(pq)
        if distance[node] < dist:
            continue
        for a, b, c in road:
            if a == node and dist + c < distance[b]:
                distance[b] = dist + c
                heapq.heappush(pq, (dist + c, b))
            elif b == node and dist + c < distance[a]:
                distance[a] = dist + c
                heapq.heappush(pq, (dist + c, a))
            else:
                continue
    for x in distance:
        if x <= K:
            answer += 1
    return answer