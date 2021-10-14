"""
input :
10
1 5 2 1 4 3 4 5 2 1

output :
7
"""
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    dp1 = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i]:
                dp1[i] = max(dp1[i], dp1[j] + 1)

    dp2 = [1 for _ in range(N)]
    for i in range(N - 1, -1, -1):
        for j in range(i + 1, N):
            if nums[j] < nums[i]:
                dp2[i] = max(dp2[i], dp2[j] + 1)

    mxv = -1
    for i in range(N):
        mxv = max(mxv, dp1[i] + dp2[i] - 1)
    print(mxv)
