"""
input :
10
2 6 4 9 6 0 2 6 1 5
3
2 5 7
1
5

output :
5 14
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))
    K = int(input())
    intervals = list(map(int, input().rstrip().split()))
    S = int(input())
    stones = list(map(int, input().rstrip().split()))
    stones.sort()

    cum_sum = [0]
    tot = 0
    for num in nums:
        tot += num
        cum_sum.append(tot)
    # print(cum_sum)

    mxv = 0
    interval_of_mxv = 0
    for interval in intervals:
        l = 0
        r = l + interval - 1
        tmp_mxv = 0
        idx = 0
        while r < len(nums):
            if idx < len(stones) and l <= stones[idx] - 1 <= r:
                l = stones[idx]
                r = l + interval - 1
                idx += 1
                continue

            tmp_mxv = max(tmp_mxv, cum_sum[r + 1] - cum_sum[l])
            l += 1
            r += 1
        if mxv < tmp_mxv:
            mxv = tmp_mxv
            interval_of_mxv = interval

    print(interval_of_mxv, mxv)
