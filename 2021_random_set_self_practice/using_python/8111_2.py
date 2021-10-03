"""
input :
17

output :
11101
"""
import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def mk_nxt(cur, N):
    nxt1 = (cur * (10 % N)) % N
    nxt2 = (cur * (10 % N) + 1) % N
    return (0, nxt1), (1, nxt2)


def bfs(N):
    que = deque()

    que.append((1, 1))  # bin, nmb
    pre_bin = [-1 for _ in range(N)]
    pre_nmb = [-1 for _ in range(N)]
    while que:
        cur_bin, cur_nmb = que.popleft()
        for nxt_bin, nxt_nmb in mk_nxt(cur_nmb, N):
            if pre_bin[nxt_nmb] != -1: continue

            pre_bin[nxt_nmb] = cur_bin
            pre_nmb[nxt_nmb] = cur_nmb
            que.append((nxt_bin, nxt_nmb))
            if nxt_nmb == 0:
                return pre_bin, pre_nmb, nxt_bin


def mk_path(preb, pren, goal):
    dq = deque([goal])
    dq.appendleft(preb[0])

    p = pren[0]
    while p != 1:
        dq.appendleft(preb[p])
        p = pren[p]
    return dq


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        if N == 1:
            print(1)
        else:
            pre_bin, pre_nmb, goal = bfs(N)

            ans = mk_path(pre_bin, pre_nmb, goal)
            print(''.join(list(map(str, ans))))
