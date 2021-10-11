"""
input :
4
2
6
12
18

output :
5
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


if __name__ == "__main__":
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    diff = [nums[i] - nums[i - 1] for i in range(1, N)]

    g = gcd(diff[0], diff[1])
    if len(diff) >= 3:
        for i in range(2, len(diff)):
            g = gcd(g, diff[i])

    tot = 0
    for d in diff:
        tot += (d // g) - 1
    print(tot)
