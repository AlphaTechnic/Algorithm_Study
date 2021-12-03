"""
input :
5 3
1 2
4 5
5 1

output :
2
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find(a):
    if par[a] == -1:
        return a
    par[a] = find(par[a])
    return par[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False

    if height[a] < height[b]:
        a, b = b, a
    par[b] = a

    if height[a] == height[b]:
        height[a] += 1

    return True


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())

    merge_cnt = 0

    par = [-1 for _ in range(N + 1)]
    height = [0 for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        if union(a, b):
            merge_cnt += 1

    print(N - merge_cnt)
