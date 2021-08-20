"""
input :
3
3 4 5
2 5 2
5 2 2

output :
1
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 1000000001


def bfs(limit):
    visited = [[False for _ in range(N)] for _ in range(N)]
    que = deque()
    que.append((heights[0][0], 0, 0))
    visited[0][0] = True

    while que:
        ch, cy, cx = que.popleft()
        for dy, dx in move:
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < N and 0 <= nx < N): continue
            if visited[ny][nx]: continue
            if abs(heights[ny][nx] - ch) > limit: continue

            visited[ny][nx] = True
            if (ny, nx) == (N - 1, N - 1):
                return True
            que.append((heights[ny][nx], ny, nx))

    return False


if __name__ == "__main__":
    N = int(input())
    heights = []
    for _ in range(N):
        heights.append(list(map(int, input().rstrip().split())))

    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    l = 0
    r = MAX
    mid_save = mid = (l + r) // 2
    while l <= r:
        if bfs(mid):
            mid_save = mid
            r = mid - 1
            mid = (l + r) // 2
        else:
            l = mid + 1
            mid = (l + r) // 2

    print(mid_save)
