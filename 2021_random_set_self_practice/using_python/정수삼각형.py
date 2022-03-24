def solution(dp):
    for i in range(len(dp)):
        for j in range(i + 1):
            a = dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
            b = dp[i - 1][j] if i - 1 >= 0 and j < i else 0
            dp[i][j] = max(a, b) + dp[i][j]
    # print(dp)

    return max(dp[-1])


if __name__ == "__main__":
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
