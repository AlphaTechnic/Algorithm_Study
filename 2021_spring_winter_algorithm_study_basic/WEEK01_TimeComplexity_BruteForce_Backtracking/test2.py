import sys

sys.setrecursionlimit(5000)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    move = [(5, 7), (6, 6), (7, 5), (8, 4), (9, 3), (10, 2), (11, 1), (12, 0)]

    max_cnt = 0
    cnt = 0


    def dfs():
        global cnt
        global max_cnt
        global A
        global B
        if A <= 0:
            max_cnt = max(max_cnt, cnt)
            return
        if B <= 0:
            cnt += A // 12
            max_cnt = max(max_cnt, cnt)
            return

        for da, db in move:
            if A - da < 0: continue
            if B - db < 0: continue

            cnt += 1
            A, B = A - da, B - db
            dfs()

            cnt -= 1
            A, B = A + da, B + db


    dfs()
    print(max_cnt)
