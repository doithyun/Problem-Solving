from itertools import permutations
from math import sqrt

def isprime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
        

def solution(numbers):
    answer = 0
    prime = set()
    for i in range(1, len(numbers) + 1):
        num = list(map(int, map("".join, permutations(numbers, i))))
        for candidate in num:
            if isprime(candidate) and candidate not in prime:
                prime.add(candidate)
                answer += 1
    return answer