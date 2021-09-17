"""
input :
3 3 2 1
2 1 0
1 0 1
2 1 2

output :
2
"""
import sys
from itertools import combinations
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def split_combi(arr, a):
    grp_a = list(combinations(arr, a))
    grp_b = []
    for grp in grp_a:
        grp_b.append(tuple(set(arr) - set(grp)))
    return zip(grp_a, grp_b)


def bfs(grp_a, grp_b):
    cnt = 0
    global R, C
    que = deque()
    vis = [[0 for _ in range(C)] for _ in range(R)]
    color = [['_' for _ in range(C)] for _ in range(R)]

    for sy, sx in grp_a:
        vis[sy][sx] = 1
        color[sy][sx] = 'a'
        que.append((sy, sx))
    for sy, sx in grp_b:
        vis[sy][sx] = 1
        color[sy][sx] = 'b'
        que.append((sy, sx))

    while que:
        cy, cx = que.popleft()
        cur_color = color[cy][cx]
        if cur_color == 'f': continue

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < R and 0 <= nx < C): continue
            if board[ny][nx] == '0': continue
            if color[ny][nx] == cur_color: continue
            if color[ny][nx] == 'f': continue

            if vis[ny][nx] == vis[cy][cx] + 1 and color[ny][nx] != '_':
                color[ny][nx] = 'f'
                cnt += 1
            elif vis[ny][nx] == 0:
                vis[ny][nx] = vis[cy][cx] + 1
                color[ny][nx] = cur_color
                que.append((ny, nx))

    return cnt


if __name__ == "__main__":
    R, C, a, b = map(int, input().rstrip().split())
    board = []
    for _ in range(R):
        board.append(list(input().rstrip().split()))

    pos2 = []
    for r in range(R):
        for c in range(C):
            if board[r][c] == '2':
                pos2.append((r, c))

    max_val = 0
    combis = list(combinations(pos2, a + b))
    for combi in combis:
        splits = split_combi(combi, a)
        for grp_a, grp_b in splits:
            max_val = max(max_val, bfs(grp_a, grp_b))
            max_val = max_val

    print(max_val)
