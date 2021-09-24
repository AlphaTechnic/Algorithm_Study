"""
iunput :
ACAYKP
CAPCAK

output :
4
ACAK
"""
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    text1 = input().rstrip()
    text2 = input().rstrip()
    l1 = len(text1)
    l2 = len(text2)
    text1 = '_' + text1
    text2 = '_' + text2

    # LCS의 길이 구하기
    dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[l1][l2])

    # dp 역추적
    ans = deque()
    i = l1
    j = l2
    while i != 0 and j != 0:
        if text1[i] == text2[j]:
            ans.appendleft(text1[i])
            i -= 1
            j -= 1
        elif text1[i] != text2[j]:
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            elif dp[i][j] == dp[i][j - 1]:
                j -= 1

    for ch in ans:
        print(ch, end='')
    print()
