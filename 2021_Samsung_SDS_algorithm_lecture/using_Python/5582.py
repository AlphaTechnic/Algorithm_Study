"""
input :
ABRACADABRA
ECADADABRBCRDARA

output :
5
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


if __name__ == "__main__":
    A = input().rstrip()
    B = input().rstrip()

    # dp[i][j] = B[i]를 마지막 원소로 넣고, A[j]를 마지막 원소로 넣을 때, 최대 공통 연속 부분 수열의 길이
    dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

    A = '_' + A
    B = '_' + B
    max_val = -1
    for i in range(1, len(B)):
        for j in range(1, len(A)):
            if A[j] == B[i]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = 0
            max_val = max(max_val, dp[i][j])

    print(max_val)