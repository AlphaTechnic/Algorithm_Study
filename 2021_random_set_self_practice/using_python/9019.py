"""
input :
3
1234 3412
1000 1
1 16

output :
LL
L
DDDD
"""
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def make_nxt(i, cur):
    if i == 0:
        return (2 * cur) % 10000
    if i == 1:
        return (cur - 1) % 10000
    if i == 2:
        pos1000 = cur // 1000
        cur = cur * 10 + pos1000
        cur %= 10000
        return cur
    if i == 3:
        pos1 = cur % 10
        cur = pos1 * 10000 + cur
        cur //= 10
        return cur


def bfs(s, tar):
    que = deque()
    vis = dict()
    que.append(s)
    vis[s] = (-1, -1)
    while que:
        cur = que.popleft()
        for i in range(4):
            nxt = make_nxt(i, cur)
            if nxt in vis: continue

            vis[nxt] = (i, cur)
            que.append(nxt)
            if nxt == tar:
                return vis


if __name__ == "__main__":
    t2ch = {0: 'D', 1: 'S', 2: 'L', 3: 'R'}
    T = int(input())
    for _ in range(T):
        S, TAR = map(int, input().rstrip().split())
        bfs_path = bfs(S, TAR)

        ans = deque()
        cur = TAR
        while cur != S:
            i, pre = bfs_path[cur]
            ans.appendleft(t2ch[i])
            cur = pre

        print(''.join(ans))
