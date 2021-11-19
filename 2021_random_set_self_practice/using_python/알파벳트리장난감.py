"""
input :
3
A
BC
DEFG

output :
7
11
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

scores = dict()
for i in range(65, 91):
    scores[chr(i)] = i - 64

MNV = 10 ** 9
MXV = -1


def dfs(cur, tot):
    global MNV, MXV

    if cur >= len(graph):
        MNV = min(MNV, tot)
        MXV = max(MXV, tot)
        return

    for nxt in (2 * cur, 2 * cur + 1):
        if nxt >= len(graph):
            dfs(nxt, tot)
            break
        else:
            dfs(nxt, tot + scores[graph[nxt]])


if __name__ == "__main__":
    N = int(input())

    graph = ['_']
    for _ in range(N):
        chs = input().rstrip()
        for ch in chs:
            graph.append(ch)

    dfs(1, scores[graph[1]])
    print(MNV)
    print(MXV)
