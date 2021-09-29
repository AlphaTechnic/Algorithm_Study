"""
input :
4 2
9 8 7 1

output :
1 1
1 7
1 8
1 9
7 1
7 7
7 8
7 9
8 1
8 7
8 8
8 9
9 1
9 7
9 8
9 9
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def recur(seq):
    global N, M
    if len(seq) == M:
        print(' '.join(list(map(str, seq))))
        return

    for i in range(N):
        seq.append(nums[i])
        recur(seq)
        seq.pop()


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    nums.sort()
    recur([])
