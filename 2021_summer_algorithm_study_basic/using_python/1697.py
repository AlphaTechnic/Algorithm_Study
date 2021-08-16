"""
input :
5 17

output :
4
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(cur):
    global K
    cnt = 0

    visited = set()
    que = deque()
    que.append([cur, cnt])

    visited.add(cur)
    while que:
        cur, cnt = que.popleft()
        nxts = [cur + 1, cur - 1, 2 * cur]
        for nxt in nxts:
            if nxt in visited: continue
            # K == 100000일 때, *2 -> -1 -> -1이 최적일 수가 없다.
            # 같은 목표에 도달하는 데 -1 -> *2 가 더 최적이다.
            if not 0 <= nxt < 100005: continue
            if nxt == K: return cnt + 1

            visited.add(nxt)
            que.append([nxt, cnt + 1])


if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())
    if N == K:
        print(0)
        exit()

    print(bfs(N))
