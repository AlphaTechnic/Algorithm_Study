"""
input :
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17

output :
3
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs():
    que = deque()
    visited[1] = 1
    que.append(1)
    while que:
        cur = que.popleft()
        for i in range(1, 7):
            new = cur + i
            if not 1 <= new <= 100: continue
            if visited[new]: continue

            if DOWN_S[new]:
                visited[new] = visited[cur] + 1
                new = DOWN_S[new]
                if visited[new]: continue
            elif LIFT_S[new]:
                visited[new] = visited[cur] + 1
                new = LIFT_S[new]
                if visited[new]: continue

            visited[new] = visited[cur] + 1
            que.append(new)

            if new == 100:
                break
    return visited[100] - 1


if __name__ == "__main__":
    L, D = map(int, input().rstrip().split())
    LIFT_S = [0 for _ in range(101)]
    DOWN_S = [0 for _ in range(101)]

    for _ in range(L):
        s, e = map(int, input().rstrip().split())
        LIFT_S[s] = e
    for _ in range(D):
        s, e = map(int, input().rstrip().split())
        DOWN_S[s] = e

    visited = [0 for _ in range(101)]
    print(bfs())
