"""
input :
5 60
30 10 20 35 40
3 0 3 5 4

output :
6
"""
import sys
sys.stdin = open("input.txt", "r")


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    MEM = [0] + list(map(int, input().rstrip().split()))
    costs = [0] + list(map(int, input().rstrip().split()))
    dp = [[0 for _ in range(sum(costs) + 1)] for _ in range(N + 1)]
    res = sum(costs)

    # dp[i][j] = i번째 앱까지 봤고, cost 목표가 j인 상황에서 확보할 수 있는 최대 MEM SIZE
    for i in range(1, N + 1):
        byte = MEM[i]
        cost = costs[i]

        for j in range(1, sum(costs) + 1):
            if j < cost:  # 현재 앱을 비활성화할만큼의 cost가 충분하지 않을 경우
                dp[i][j] = dp[i - 1][j]
            else:
                # 같은 cost 내에서 현재 앱을 끈 뒤의 byte와 현재 앱을 끄지 않은 뒤의 byte를 비교
                dp[i][j] = max(byte + dp[i - 1][j - cost], dp[i - 1][j])

            if dp[i][j] >= M:  # 조건이 충족된다면
                res = min(res, j)  # 더 작은 cost값으로 갱신
    if M != 0:
        print(res)
    else:
        print(0)
