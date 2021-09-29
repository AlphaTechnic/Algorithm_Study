"""
input :
4 2
9 8 7 1

output :
1 7
1 8
1 9
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(seq):
    global N, M
    if len(seq) == M:
        print(' '.join(list(map(str, seq))))
        return

    for i in range(N):
        if is_used[i]: continue

        seq.append(nums[i])
        is_used[i] = True
        recur(seq)
        seq.pop()
        is_used[i] = False


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    nums.sort()
    is_used = [False for _ in range(N)]

    recur([])
