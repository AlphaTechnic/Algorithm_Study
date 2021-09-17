"""
input :
3 4
2 0 0 0
0 0 0 0
0 0 0 2

output :
1
"""
import sys
from collections import deque
from itertools import combinations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(pos):
    grp = list()
    que = deque()
    sy = pos[0]
    sx = pos[1]
    visited[sy][sx] = True
    grp.append((sy, sx))
    que.append((sy, sx))
    while que:
        cy, cx = que.popleft()
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < R and 0 <= nx < C): continue
            if visited[ny][nx]: continue
            if board[ny][nx] != '2': continue

            grp.append((ny, nx))
            que.append((ny, nx))
            visited[ny][nx] = True
    return grp


def put_two_stones(combi):
    y1, x1 = combi[0]
    y2, x2 = combi[1]
    board[y1][x1] = '1'
    board[y2][x2] = '1'


def chk_cnt(grp):
    cnt = 0
    for cy, cx in grp:
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < R and 0 <= nx < C): continue
            if board[ny][nx] == '0':
                return 0
        cnt += 1
    return cnt


def restore(combi):
    y1, x1 = combi[0]
    y2, x2 = combi[1]
    board[y1][x1] = '0'
    board[y2][x2] = '0'


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = list()
    for _ in range(R):
        board.append(input().rstrip().split())

    # 돌을 놓을 수 있는 위치 모아둠
    poses = list()
    for r in range(R):
        for c in range(C):
            if board[r][c] == '0':
                poses.append((r, c))

    # connected component 정리
    visited = [[False for _ in range(C)] for _ in range(R)]
    grps = list()
    for r in range(R):
        for c in range(C):
            if visited[r][c]: continue
            if board[r][c] == '2':
                grp = bfs((r, c))
                grps.append(grp)

    combis = list(combinations(poses, 2))
    max_val = -1
    for combi in combis:
        # 바둑돌 2개 놓기
        put_two_stones(combi)

        # 몇개나 잡는지 chk
        cnt = 0
        for grp in grps:
            cnt += chk_cnt(grp)
        max_val = max(max_val, cnt)

        # 원상 복구
        restore(combi)

    print(max_val)
