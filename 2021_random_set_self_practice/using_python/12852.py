"""
input :
10

output :
3
10 9 3 1
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def make_nxt(type, cur):
    if type == 0 and cur % 3 == 0:
        return cur // 3, "*3"
    elif type == 1 and cur % 2 == 0:
        return cur // 2, "*2"
    elif type == 2:
        return cur - 1, "+1"

    return -1, '_'


def bfs(N):
    que = deque()
    que.append((N, '_'))
    visited[N] = (0, '+1')
    while que:
        cur, _ = que.popleft()
        for i in range(3):
            nxt, inv_op = make_nxt(i, cur)
            if nxt == -1: continue
            if visited[nxt]: continue

            visited[nxt] = (visited[cur][0] + 1, inv_op)
            que.append((nxt, inv_op))
            if nxt == 1:
                return


def update(num, op):
    if op == '*3':
        return num * 3
    elif op == '*2':
        return num * 2
    elif op == '+1':
        return num + 1


if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print(0)
        print(1)
        exit(0)

    visited = [False for _ in range(N + 1)]
    bfs(N)

    # print ans
    ind = 1
    print(visited[1][0])

    ans = deque()
    while True:
        _, op = visited[ind]
        ans.appendleft(ind)
        ind = update(ind, op)

        if ind == N:
            ans.appendleft(ind)
            break

    for num in ans:
        print(num, end=' ')
    print()
