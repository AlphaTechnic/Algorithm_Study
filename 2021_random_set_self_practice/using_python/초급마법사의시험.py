"""
input :
5 5 10
01100
01100
01010
00010
00110

output :
7
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


class BFS():
    def __init__(self, bd, K):
        self.bd = bd
        self.K = K // 10
        self.R = len(bd)
        self.C = len(bd[0])

    def execute(self):
        que = deque()  # cy, cx, 직전에 마법을 썻는지에 대한 유무, 남은 마력
        que.append((0, 0, self.K))
        vis = [[[0 for _ in range(self.K + 1)] for _ in range(self.C + 1)] for _ in range(self.R + 1)]
        vis[0][0][self.K] = 1

        while que:
            cy, cx, remain = que.popleft()
            if (cy, cx) == (self.R - 1, self.C - 1):
                return vis[cy][cx][remain] - 1

            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny, nx = cy + dy, cx + dx
                if not 0 <= ny < self.R: continue
                if not 0 <= nx < self.C: continue

                if bd[ny][nx] == '0' and not vis[ny][nx][remain]:
                    que.append((ny, nx, remain))
                    vis[ny][nx][remain] = vis[cy][cx][remain] + 1
                elif bd[ny][nx] == '1':
                    nny, nnx = ny + dy, nx + dx
                    if not 0 <= nny < self.R: continue
                    if not 0 <= nnx < self.C: continue
                    if bd[nny][nnx] == '1': continue

                    if remain >= 1 and not vis[ny][nx][remain - 1]:
                        que.append((nny, nnx, remain - 1))
                        vis[nny][nnx][remain - 1] = vis[cy][cx][remain] + 1
        return -1


if __name__ == "__main__":
    R, C, K = map(int, input().rstrip().split())
    bd = [input().rstrip() for _ in range(R)]
    res = BFS(bd, K).execute()
    print(res)
