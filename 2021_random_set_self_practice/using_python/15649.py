"""
input :
4 2

output :
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(seq):
    global N, M
    if len(seq) == M:
        for n in seq:
            print(n, end=' ')
        print()
        return

    for i in range(1, N + 1):
        if vis[i]: continue

        seq.append(i)
        vis[i] = True

        recur(seq)

        seq.pop()
        vis[i] = False


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())

    ans = []
    vis = [False for _ in range(N + 1)]
    recur([])
