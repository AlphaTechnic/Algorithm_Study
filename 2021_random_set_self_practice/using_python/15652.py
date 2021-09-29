"""
input :
4 2

output :
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def recur(n, seq):
    global N, M
    if len(seq) == M:
        print(' '.join(list(map(str, seq))))
        return

    for i in range(n, N + 1):
        if len(seq) >= 1 and seq[-1] > i: continue

        seq.append(i)
        recur(n, seq)
        seq.pop()


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    is_used = [False for _ in range(N + 1)]
    recur(1, [])
