"""
input :
17

output :
11101
"""
import sys
from collections import deque
from collections import defaultdict

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def mk_nxt(cur, N):
    nxt1 = (cur * (10 % N)) % N
    nxt2 = (cur * (10 % N) + 1) % N
    return (0, nxt1), (1, nxt2)


def bfs(N):
    que = deque()
    pre = defaultdict(int)

    que.append((1, 1))  # bin, nmb
    pre[(1, 1)] = (-1, -1)
    while que:
        cur_bin, cur_nmb = que.popleft()
        for nxt_bin, nxt_nmb in mk_nxt(cur_nmb, N):
            if pre[(nxt_bin, nxt_nmb)]: continue

            pre[(nxt_bin, nxt_nmb)] = (cur_bin, cur_nmb)
            que.append((nxt_bin, nxt_nmb))
            if nxt_nmb == 0:
                return pre, nxt_bin


def mk_path(pre, goal):
    dq = deque([goal])
    b, n = pre[(goal, 0)]
    dq.appendleft(b)

    pb, pn = pre[(b, n)]
    while (pb, pn) != (-1, -1):
        dq.appendleft(pb)
        pb, pn = pre[(pb, pn)]

    return dq


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        if N == 1:
            print(1)
        else:
            pre, goal = bfs(N)

            ans = mk_path(pre, goal)
            print(''.join(list(map(str, ans))))
