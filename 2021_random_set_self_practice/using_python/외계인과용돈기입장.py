"""
input :
5 3
+7 +2 -6 +5 -9
1 5
2 2
3 5

output :
-1
+2
-10
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, Q = map(int, input().rstrip().split())
    nums = [0] + list(map(int, input().rstrip().split()))

    cum_sum = []
    tot = 0
    for i in range(len(nums)):
        tot += nums[i]
        cum_sum.append(tot)

    for _ in range(Q):
        a, b = map(int, input().rstrip().split())
        ans = cum_sum[b] - cum_sum[a - 1]
        print(f"+{ans}") if ans >= 0 else print(ans)
