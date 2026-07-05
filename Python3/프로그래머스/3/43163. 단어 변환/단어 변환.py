from collections import deque
def solution(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    if target not in words:
        return 0
    else:
        visited = [False] * len(words)
        while(queue):
            [word, depth] = queue.popleft()
            for idx, candidate in enumerate(words):
                cnt = 0
                for i in range(len(word)):
                    if(word[i] != candidate[i]):
                        cnt += 1
                if cnt == 1 and not visited[idx]:
                    queue.append([candidate, depth + 1])
                    visited[idx] = True
                    if candidate == target:
                        return depth + 1