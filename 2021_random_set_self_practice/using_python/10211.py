"""
input :
2
5
1 2 3 4 5
5
2 1 -2 3 -5

output :
4
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        nums = list(map(int, input().rstrip().split()))
        cum_tot = [0] + []
        tot = 0
        for num in nums:
            tot += num
            cum_tot.append(tot)

        mxv = -10 ** 9
        for i in range(N + 1):
            for j in range(i + 1, N + 1):
                if cum_tot[j] - cum_tot[i] > mxv:
                    mxv = cum_tot[j] - cum_tot[i]
        print(mxv)
