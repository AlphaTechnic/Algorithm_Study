"""
input :
5 6
-1 1 2 3 4
1 2 2
1 3 4
1 4 6
2 5
2 3
2 1

output :
0
10
12
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
PIV = 1 << 17
tree = [0 for _ in range(2 * PIV)]


def update(ind, val):
    ind += PIV
    tree[ind] += val

    while True:
        ind >>= 1
        if ind == 0: break
        tree[ind] += val


def query(l, r):
    l += PIV; r += PIV;
    ret = 0
    while l <= r:
        if l & 1:
            ret += tree[l]
            l += 1
        if not r & 1:
            ret += tree[r]
            r -= 1
        l >>= 1; r >>= 1;
    return ret


def dfs(s):
    global dfn
    dfn += 1
    dfs_in[s] = dfn
    visited[s] = True
    for nxt in graph[s]:
        if visited[nxt]: continue
        dfs(nxt)
    dfs_out[s] = dfn


if __name__ == "__main__":
    N, Q = map(int, input().rstrip().split())
    parent = list(map(int, input().rstrip().split()))

    graph = [[] for _ in range(N + 1)]
    for i, parent in enumerate(parent):
        if parent == -1: continue
        graph[parent].append(i + 1)

    dfn = 0
    dfs_in = [0 for _ in range(N + 1)]
    dfs_out = [0 for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    dfs(1)

    # 쿼리 수행
    for _ in range(Q):
        line = list(map(int, input().rstrip().split()))
        if line[0] == 1:
            update(dfs_in[line[1]], line[2])
        elif line[0] == 2:
            print(query(dfs_in[line[1]], dfs_out[line[1]]))
