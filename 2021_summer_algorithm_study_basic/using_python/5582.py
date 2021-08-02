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
    A = '_' + input().rstrip()
    B = '_' + input().rstrip()

    dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

    max_val = 0
    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if A[i] == B[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0
            max_val = max(max_val, dp[i][j])
    print(max_val)
