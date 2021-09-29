"""
input :
4 2
9 7 9 1

output :
1 7
1 9
7 1
7 9
9 1
9 7
9 9
"""
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def recur(seq):
    if len(seq) == M:
        print(' '.join(list(map(str, seq))))
        return

    pre = 0
    for i in range(N):
        if is_used[i]: continue
        if pre == nums[i]: continue

        seq.append(nums[i])
        is_used[i] = True
        pre = nums[i]
        recur(seq)
        seq.pop()
        is_used[i] = False


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    nums.sort()
    is_used = [False for _ in range(N)]

    recur([])
