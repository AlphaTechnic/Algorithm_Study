def reverse_board(board):
    R = len(board)
    C = len(board[0])
    return [[board[i][j] ^ 1 for j in range(C)] for i in range(R)]


def rotate(board):
    return [col[::-1] for col in zip(*board)]


def cpy_board(board):
    return [row[:] for row in board]


def extract(board, sy, sx, length):
    y1, x1 = sy, sx
    y2, x2 = sy + length, sx + length
    new_board = [board[y][x1:x2] for y in range(y1, y2)]
    return new_board


def is_equal(board1, board2, cnt_hole):
    R = len(board1)
    C = len(board1[0])

    cnt = 0
    for i in range(R):
        for j in range(C):
            if board2[i][j] == '_':
                continue
            if board1[i][j] != board2[i][j]:
                return False
            if board1[i][j] == 1:
                cnt += 1
    if cnt == cnt_hole:
        return True
    return False


def is_matched(key_rotated, new_lock, cnt_hole):
    move_y, move_x = len(new_lock) // 3, len(new_lock[0]) // 3
    for sy in range(1, 2 * move_y):
        for sx in range(1, 2 * move_x):
            new_board = extract(new_lock, sy, sx, len(new_lock) // 3)
            if is_equal(key_rotated, new_board, cnt_hole):
                return True
    return False


def solution(key, lock):
    lock = reverse_board(lock)
    length = len(lock)
    new_lock = [['_' for _ in range(3 * length)] for _ in range(3 * length)]
    cnt_hole = 0
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            new_lock[i + length][j + length] = lock[i][j]
            if lock[i][j] == 1:
                cnt_hole += 1

    key_rotated = cpy_board(key)
    for _ in range(4):
        if is_matched(key_rotated, new_lock, cnt_hole):
            return True
        key_rotated = rotate(key_rotated)
    return False


if __name__ == "__main__":
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
