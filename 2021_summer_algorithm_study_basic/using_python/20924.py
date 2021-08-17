"""
input :
12 1
1 2 1
2 3 2
3 4 3
4 5 1
5 6 2
6 7 1
5 8 1
4 9 2
4 10 3
10 11 1
10 12 3

output :
6 6
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def find_giga(R):
    cur = R
    tot = 0
    while True:
        if len(dfs_tree[cur]) >= 2:
            return cur, tot
        if len(dfs_tree[cur]) == 0:
            return cur, tot

        tot += dfs_tree[cur][0][1]
        cur = dfs_tree[cur][0][0]


def find_branch_len(GIGA_ND, tot):
    global MAX_VAL
    if len(dfs_tree[GIGA_ND]) == 0:
        MAX_VAL = max(MAX_VAL, tot)
        return

    for nxt, c in dfs_tree[GIGA_ND]:
        find_branch_len(nxt, tot + c)


def dfs_for_restruct(p, mp):
    for chd, c in graph[p]:
        if chd == mp: continue

        dfs_tree[p].append((chd, c))
        dfs_for_restruct(chd, p)


if __name__ == "__main__":
    V, R = map(int, input().rstrip().split())
    graph = dict()
    for i in range(1, V + 1):
        graph[i] = list()

    for _ in range(V - 1):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    dfs_tree = dict()
    for i in range(1, V + 1):
        dfs_tree[i] = list()
    visited = [False for _ in range(V + 1)]
    dfs_for_restruct(R, -1)

    PILLAR_LEN = 0
    GIGA_ND, PILLAR_LEN = find_giga(R)

    MAX_VAL = 0
    BRANCH_LEN = find_branch_len(GIGA_ND, 0)
    print(PILLAR_LEN, MAX_VAL)
