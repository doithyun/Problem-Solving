from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(v, i) for i, v in enumerate(priorities)])
    
    while q:
        item = q.popleft()
        if any(item[0] < other[0] for other in q):
            q.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
                
    return answer