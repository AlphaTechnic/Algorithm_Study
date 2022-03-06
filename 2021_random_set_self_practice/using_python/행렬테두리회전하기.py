from collections import deque


def mk_seq1(board, piv, start, end):
    ret = []
    for c in range(start, end):
        ret.append(board[piv][c])
    return ret


def mk_seq2(board, piv, start, end):
    ret = []
    for r in range(start, end):
        ret.append(board[r][piv])
    return ret


def mk_seq3(board, piv, start, end):
    ret = []
    for c in range(start, end, -1):
        ret.append(board[piv][c])
    return ret


def mk_seq4(board, piv, start, end):
    ret = []
    for r in range(start, end, -1):
        ret.append(board[r][piv])
    return ret


def action(board, seq, y1, x1, y2, x2):
    pos = 0

    piv = y1
    for c in range(x1, x2):
        board[piv][c] = seq[pos]
        pos += 1

    piv = x2
    for r in range(y1, y2):
        board[r][piv] = seq[pos]
        pos += 1

    piv = y2
    for c in range(x2, x1, -1):
        board[piv][c] = seq[pos]
        pos += 1

    piv = x1
    for r in range(y2, y1, -1):
        board[r][piv] = seq[pos]
        pos += 1


def solution(rows, columns, queries):
    board = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
    num = 1
    for r in range(1, rows + 1):
        for c in range(1, columns + 1):
            board[r][c] = num
            num += 1

    ans = []
    for y1, x1, y2, x2 in queries:
        row1 = mk_seq1(board, y1, x1, x2)
        col1 = mk_seq2(board, x2, y1, y2)
        row2 = mk_seq3(board, y2, x2, x1)
        col2 = mk_seq4(board, x1, y2, y1)

        seq = row1 + col1 + row2 + col2
        seq = deque(seq)
        seq.rotate(1)
        ans.append(min(seq))

        action(board, seq, y1, x1, y2, x2)
    return ans


if __name__ == "__main__":
    print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
