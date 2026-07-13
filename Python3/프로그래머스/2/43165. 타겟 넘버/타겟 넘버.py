def solution(numbers, target):
    def dfs(sum, step):
        if step == len(numbers):
            if sum == target:
                return 1
            else:
                return 0
        else:
            return dfs(sum + numbers[step], step + 1) + dfs(sum - numbers[step], step + 1)
    return dfs(0, 0)