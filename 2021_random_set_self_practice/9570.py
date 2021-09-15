"""
input :
8
0
1
2
3
4
5
30
67

output :
1
1
2
4
8
15
201061985
7057305768232953720
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    dp = [1 for _ in range(70)]
    dp[2] = 2
    dp[3] = 4
    for i in range(4, 70):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

    T = int(input())
    for _ in range(T):
        N = int(input())
        print(dp[N])
