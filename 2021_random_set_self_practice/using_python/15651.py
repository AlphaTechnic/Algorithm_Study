"""
input :
4 2

output :
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(seq):
    global N, M
    if len(seq) == M:
        print(' '.join(list(map(str, seq))))
        return

    for i in range(1, N + 1):
        seq.append(i)
        recur(seq)
        seq.pop()


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    recur([])
