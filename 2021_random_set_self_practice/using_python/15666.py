"""
input :
4 2
9 7 9 1

output :
1 1
1 7
1 9
7 7
7 9
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
        if len(seq) >= 1 and seq[-1] > nums[i]: continue

        seq.append(nums[i])
        recur(seq)
        seq.pop()


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    nums = list(set(nums))

    nums.sort()
    N = len(nums)

    recur([])
