"""
input :
6 10
..x.......
.....x....
.x....x...
...x...xx.
..........
....x.....

output :
5
"""
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def dfs(sy, sx):
    st = list()
    st.append([sy, sx])

    while st:
        cy, cx = st.pop()
        board[cy][cx] = 'x'
        for dy, dx in move:
            ny, nx = cy + dy, cx + dx

            if not (0 <= ny < R and 0 <= nx < C): continue
            if board[ny][nx] == 'x': continue

            if nx == C - 1:  # 종료 조건
                board[cy][cx] = 'x'
                return 1
            st.append([ny, nx])
    return 0


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = []
    for _ in range(R):
        board.append(list(input().strip()))

    cnt = 0
    # move의 앞부터 순회하면서 stack에 집어넣고 다시 stack의 꼭대기에서 빼기 때문에
    # move의 맨 뒤의 원소인 dy, dx에 영향을 받은 좌표를 가장 먼저 접근하게 된다.
    move = [[1, 1], [0, 1], [-1, 1]]
    for r in range(R):
        cnt += dfs(r, 0)
    print(cnt)
