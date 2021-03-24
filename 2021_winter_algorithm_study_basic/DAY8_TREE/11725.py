import sys
sys.stdin = open("input.txt", "r")
import collections


def bfs(start, check, tree):
    que = collections.deque([start])
    ans = {}
    while que:
        parent = que.popleft()

        for i in tree[parent]:
            if not check[i]:
                que.append(i)
                check[i] = True
                ans[i] = parent

    for i in range(2, N+1):
        print(ans[i])

input = sys.stdin.readline
N = int(input())

tree = [[] for _ in range(N+1)]
check = [False for _ in range(N+1)]

for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

bfs(1, check, tree)