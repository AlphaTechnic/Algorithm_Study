class Pos(object):
    def __init__(self, type: str):
        self.type = type
        self.visited = [False for _ in range(4)]

    def mark_visited(self, input_direction):
        self.visited[input_direction] = True
        return True

    def is_visited(self, input_direction):
        return self.visited[input_direction]

    def __str__(self):
        return f"{self.type}"


class Board(object):
    nextInputDirection = {
        'S': {0: 0, 1: 1, 2: 2, 3: 3},
        'R': {0: 1, 1: 2, 2: 3, 3: 0},
        'L': {0: 3, 1: 0, 2: 1, 3: 2},
    }
    nextPosition = {
        0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)
    }

    def __init__(self, board):
        self.R = len(board)
        self.C = len(board[0])
        self.board = [[Pos('_') for _ in range(self.C)] for _ in range(self.R)]
        for i in range(self.R):
            for j in range(self.C):
                self.board[i][j] = Pos(board[i][j])

    def travel(self):
        ans = []

        directions = []
        for r in range(self.R):
            for c in range(self.C):
                for i in range(4):
                    if self.board[r][c].is_visited(i):
                        continue

                    y = r
                    x = c
                    input_direction = i
                    while True:
                        y, x, input_direction = self.move(y, x, input_direction)
                        if input_direction == -1:
                            if len(directions) != 0:
                                ans.append(len(directions))
                            directions = []
                            break
                        directions.append(input_direction)
        return sorted(ans)

    def move(self, y, x, input_direction):
        if self.board[y][x].is_visited(input_direction):
            return -1, -1, -1

        self.board[y][x].mark_visited(input_direction)
        type = self.board[y][x].type
        nxt_input_direction = Board.nextInputDirection[type][input_direction]
        return (y + Board.nextPosition[nxt_input_direction][0]) % self.R, \
                (x + Board.nextPosition[nxt_input_direction][1]) % self.C, nxt_input_direction


def solution(grid):
    board = Board(grid)
    ans = board.travel()
    return ans


if __name__ == "__main__":
    print(solution(["SS"]))
