def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    second = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)
    f = sum(1 for x, y in zip(answers, first) if x == y)
    s = sum(1 for x, y in zip(answers, second) if x == y)    
    t = sum(1 for x, y in zip(answers, third) if x == y)
    if f == max(f,s,t):
        answer.append(1)
    if s == max(f,s,t):
        answer.append(2)
    if t == max(f,s,t):
        answer.append(3)
    return answer