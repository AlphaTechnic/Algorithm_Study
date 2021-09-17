"""
input :
1 2 2 4 0

output :
8
"""
import sys
sys.setrecursionlimit(10 ** 7)
sys.stdin = open("input.txt")
input = sys.stdin.readline

# cost[from][to]
cost = [
    [0, 2, 2, 2, 2],
    [0, 1, 3, 4, 3],
    [0, 3, 1, 3, 4],
    [0, 4, 3, 1, 3],
    [0, 3, 4, 3, 1],
]
MAX = 10 ** 9


def recur(ind, l, r):
    if ind == N:
        return 0
    if (ind, l, r) in dp:
        return dp[(ind, l, r)]

    case1 = case2 = MAX
    if qs[ind] != r:
        case1 = recur(ind + 1, qs[ind], r) + cost[l][qs[ind]]
    if qs[ind] != l:
        case2 = recur(ind + 1, l, qs[ind]) + cost[r][qs[ind]]
    dp[(ind, l, r)] = min(case1, case2)
    return dp[(ind, l, r)]


if __name__ == "__main__":
    qs = list(map(int, input().rstrip().split()))
    qs.pop()
    N = len(qs)
    dp = dict()

    print(recur(0, 0, 0))
