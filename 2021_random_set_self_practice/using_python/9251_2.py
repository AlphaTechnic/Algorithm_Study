"""
input :
ACAYKP
CAPCAK

output :
4
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    text1 = input().rstrip()
    text2 = input().rstrip()

    l1 = len(text1)
    l2 = len(text2)
    text1 = '_' + text1
    text2 = '_' + text2
    dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[l1][l2])
