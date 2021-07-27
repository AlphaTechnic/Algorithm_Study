"""
input :
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

output :
0
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


# 한 명씩 팀 A로 영입
def dfs(cnt):
    global min_val

    # 백트래킹 답 체크 시점
    if cnt == N // 2:
        tot1 = 0
        tot2 = 0
        for i in range(N):
            if not visited[i]:
                B.append(i)

        for i in range(N // 2 - 1):
            for j in range(i + 1, N // 2):
                tot1 += board[A[i]][A[j]] + board[A[j]][A[i]]
                tot2 += board[B[i]][B[j]] + board[B[j]][B[i]]
        min_val = min(min_val, abs(tot1 - tot2))

        B.clear()
        return

    # dfs
    for i in range(N):
        if visited[i]: continue
        if len(A) != 0 and A[-1] > i: continue

        visited[i] = True
        A.append(i)

        dfs(cnt + 1)

        visited[i] = False
        A.pop()


if __name__ == "__main__":
    N = int(input())

    board = []
    A = []
    B = []
    for i in range(N):
        board.append(list(map(int, input().rstrip().split())))

    min_val = 1000
    visited = [False for _ in range(N)]
    dfs(0)
    print(min_val)
