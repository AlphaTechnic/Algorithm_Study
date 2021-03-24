import sys
sys.stdin = open("input.txt", "r")

import collections

MAX = 40002
tree = [[] for _ in range(MAX)]
depth = [0 for _ in range(MAX)]
d = [0 for _ in range(MAX)]
par = [0 for _ in range(MAX)]
chk = [False for _ in range(MAX)]


def lca(a, b):
    ans = 0
    if depth[a] < depth[b]:
        a, b = b, a

    while depth[a] != depth[b]:
        ans += d[a]
        a = par[a]

    while a != b:
        ans += d[a]
        ans += d[b]
        a = par[a]
        b = par[b]

    return ans


N = int(input())
for i in range(N-1):
    u, v, c = map(int, input().split())
    tree[u].append([v, c])
    tree[v].append([u, c])


queue = collections.deque([])
chk[1] = True
queue.append(1)
while len(queue) != 0:
    x = queue.popleft()
    for i in range(len(tree[x])):
        y = tree[x][i][0]
        if chk[y] is False:
            par[y] = x
            depth[y] = depth[x] + 1
            d[y] = tree[x][i][1]
            queue.append(y)
            chk[y] = True


M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    print(lca(u, v))