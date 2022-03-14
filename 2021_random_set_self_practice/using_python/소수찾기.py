import math
from itertools import permutations
from collections import defaultdict

visited = defaultdict(bool)


def is_prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    cnt = 0
    for i in range(1, len(numbers) + 1):
        for permu in permutations(numbers, i):
            target = int(''.join(permu))
            if visited[target]:
                continue
            else:
                visited[target] = True

            if is_prime(target):
                cnt += 1

    return cnt


if __name__ == "__main__":
    print(solution("011"))
