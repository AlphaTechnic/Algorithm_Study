"""
input :
4 6 8
1 2
1 3
1 6
2 3
2 6
3 6
4 5
5 6

output :
1
2
3
6
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def print_ans():
    for mem in members:
        print(mem)


def chk_all_friends(i):
    for mem in members:
        if not adj_mat[mem][i]:
            return False
    return True


def recur(dep):
    global cnt
    if dep == N: return
    if cnt == K:
        print_ans()
        exit()

    for i in range(dep + 1, N + 1):
        if adj_mat[i][0] < K - 1: continue
        if isused[i]: continue
        if not chk_all_friends(i): continue

        isused[i] = True
        members.append(i)
        cnt += 1

        recur(dep + 1)

        isused[i] = False
        members.pop()
        cnt -= 1

        recur(dep + 1)


if __name__ == "__main__":
    K, N, F = map(int, input().rstrip().split())

    adj_mat = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for _ in range(F):
        a, b = map(int, input().rstrip().split())
        adj_mat[a][b] = 1; adj_mat[a][0] += 1
        adj_mat[b][a] = 1; adj_mat[b][0] += 1


    isused = [False for _ in range(N + 1)]
    members = []
    cnt = 0

    recur(0)
    print(-1)
