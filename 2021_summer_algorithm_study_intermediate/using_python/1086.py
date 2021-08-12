"""
input :
3
3
2
1
2

output :
1/3
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


if __name__ == "__main__":
    N = int(input())
    nums_str = []
    for _ in range(N):
        nums_str.append(input().rstrip())
    K = int(input())

    # factorial 전처리
    fact = [1, 1]
    for i in range(2, 16):
        fact.append(fact[i - 1] * i)

    # mul 전처리
    pow_of_10 = [1]
    for i in range(1, 51):
        pow_of_10.append((pow_of_10[i - 1] * 10) % K)

    # 모든 수에 대해 모듈러 처리
    nums_refined = []
    for i in range(N):
        tot = 0
        ind = 0
        for j in range(len(nums_str[i]) - 1, -1, -1):
            tot += (int(nums_str[i][j]) * pow_of_10[ind]) % K
            tot %= K
            ind += 1
        nums_refined.append(tot)

    dp = [[0 for _ in range(K)] for _ in range(1 << N)]
    dp[0][0] = 1
    for i in range(1 << N):
        for pre_remain in range(K):
            for kth in range(N):
                if (i & (1 << kth)) == 0:  # kth 숫자를 추가할 수 있는 상태
                    nxt_remain = (((pre_remain * pow_of_10[len(nums_str[kth])]) % K) + nums_refined[kth]) % K
                    dp[i | (1 << kth)][nxt_remain] += dp[i][pre_remain]

    g = gcd(dp[(1 << N) - 1][0], fact[N])
    print("%s/%s" % (dp[(1 << N) - 1][0] // g, fact[N] // g))
