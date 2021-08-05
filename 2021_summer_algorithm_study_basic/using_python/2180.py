"""
input :
3
2 0
1 2
0 3

output :
5
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 10 ** 9
MOD = 40000


def comp(a, b):
    if a == 0:
        return MAX
    return b / a


if __name__ == "__main__":
    N = int(input())
    ab = []
    for _ in range(N):
        a, b = map(int, input().rstrip().split())
        ab.append([a, b])

    ab.sort(key=lambda ab: comp(ab[0], ab[1]))
    print(ab)
    tot = 0
    for a, b in ab:
        tot += ((a * tot) % MOD + b) % MOD
    print(tot % MOD)
