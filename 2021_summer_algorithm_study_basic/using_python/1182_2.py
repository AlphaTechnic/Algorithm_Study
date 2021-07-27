"""
input :
5 0
-7 -3 -2 5 8

output :
1
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


if __name__ == "__main__":
    N, S = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))

    cnt = 0

    for i in range(1, 1 << N):
        tot = 0
        for j in range(N):
            if i & (1 << j):
                tot += nums[j]
        if tot == S:
            cnt += 1

    print(cnt)
