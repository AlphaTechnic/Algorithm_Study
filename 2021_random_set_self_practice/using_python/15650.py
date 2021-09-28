"""
input :
4 2

output :
1 2
1 3
1 4
2 3
2 4
3 4
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(idx, seq):
    global N, M
    if len(seq) == M:
        for num in seq:
            print(num, end=' ')
        print()
        return

    for i in range(idx, N + 1):
        seq.append(i)
        recur(i + 1, seq)
        seq.pop()


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())

    ans = []
    recur(1, [])
