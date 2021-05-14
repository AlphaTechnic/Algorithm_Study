"""
input :
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

output :
5
1
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def dfs(s):
    st = []
    st.append(s)
    visited[s[0]][s[1]] = True

    while len(st) != 0:
        cy, cx = st.pop()
        if not visited[cy][cx]:
            visited[cy][cx] = True

        for dy, dx in move:
            ny = cy + dy
            nx = cx + dx
            if not 0 <= ny < R: continue
            if not 0 <= nx < C: continue
            if board[ny][nx] != 1: continue
            if visited[ny][nx]: continue

            st.append([ny, nx])


T = int(input().rstrip())
for _ in range(T):
    C, R, K = map(int, input().rstrip().split())
    board = [[0 for _ in range(C)] for _ in range(R)]
    for _ in range(K):
        c, r = map(int, input().rstrip().split())
        board[r][c] = 1

    visited = [[False for _ in range(C)] for _ in range(R)]

    cnt = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1 and not visited[r][c]:
                dfs([r, c])
                cnt += 1
    print(cnt)
