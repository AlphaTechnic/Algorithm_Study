"""
input :
3 10
1
2
5

output :
10
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())
    scales = [int(input()) for _ in range(N)]

    # dp[i] = i원을 만드는 경우의 수
    dp = [0 for _ in range(K + 1)]
    dp[0] = 1
    for i in range(N):
        for j in range(scales[i], K + 1):
            dp[j] += dp[j - scales[i]]
    print(dp[K])
