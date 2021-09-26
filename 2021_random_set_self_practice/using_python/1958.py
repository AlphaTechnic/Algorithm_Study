"""
input :
abcdefghijklmn
bdefg
efg

output :
3
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    txt1 = '_' + input().rstrip()
    txt2 = '_' + input().rstrip()
    txt3 = '_' + input().rstrip()

    dp = [[[0 for _ in range(len(txt3))] for _ in range(len(txt2))] for _ in range(len(txt1))]
    for i in range(1, len(txt1)):
        for j in range(1, len(txt2)):
            for k in range(1, len(txt3)):
                if txt1[i] == txt2[j] and txt2[j] == txt3[k]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    print(dp[len(txt1) - 1][len(txt2) - 1][len(txt3) - 1])
