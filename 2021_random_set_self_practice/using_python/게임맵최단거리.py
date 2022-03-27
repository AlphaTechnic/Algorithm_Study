from collections import deque


class Graph(object):
    def __init__(self, maps):
        self.board = maps
        self.R = len(maps)
        self.C = len(maps[0])
        self.visited = [[0 for _ in range(self.C)] for _ in range(self.R)]
        self.que = deque()

    def bfs(self):
        self.que.append((0, 0))
        self.visited[0][0] = 1
        while self.que:
            cy, cx = self.que.popleft()
            if (cy, cx) == (self.R - 1, self.C - 1):
                break

            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny, nx = cy + dy, cx + dx
                if not (0 <= ny < self.R and 0 <= nx < self.C):
                    continue
                if self.board[ny][nx] == 0:  # 벽
                    continue
                if self.visited[ny][nx]:
                    continue

                self.que.append((ny, nx))
                self.visited[ny][nx] = self.visited[cy][cx] + 1
        ans = self.visited[self.R - 1][self.C - 1]
        return ans if ans != 0 else -1


def solution(maps):
    graph = Graph(maps)
    return graph.bfs()


if __name__ == "__main__":
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
