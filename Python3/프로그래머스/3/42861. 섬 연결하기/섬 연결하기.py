def solution(n, costs):
    costs = sorted(costs, key = lambda x: x[2])
    answer = costs[0][2]
    area = set()
    area.add(costs[0][0])
    area.add(costs[0][1])
    while(len(area) != n):
        for i in range(1, len(costs)):
            if (costs[i][0] in area and costs[i][1] not in area) 
                or (costs[i][1] in area and costs[i][0] not in area):
                area.add(costs[i][0])
                area.add(costs[i][1])
                answer += costs[i][2]
                break
    return answer