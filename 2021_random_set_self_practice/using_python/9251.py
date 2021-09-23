"""
input :
ACAYKP
CAPCAK

output :
4
"""
import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    text1 = input().rstrip()
    text2 = input().rstrip()

    l1 = len(text1)
    l2 = len(text2)
    dp = defaultdict(int)
    for i in range(l1):
        for j in range(l2):
            if text1[i] == text2[j]:
                dp[(i, j)] = dp[(i - 1, j - 1)] + 1
            else:
                dp[(i, j)] = max(dp[(i - 1, j)], dp[i, j - 1])
    print(dp[(l1 - 1, l2 - 1)])
