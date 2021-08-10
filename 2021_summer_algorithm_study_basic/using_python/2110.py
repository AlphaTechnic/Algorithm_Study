"""
input :
5 3
1
2
8
4
9

output :
3
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def install_router(mid):
    cnt = 1
    cur = nums[0]
    nxt = cur + mid
    for num in nums[1:]:
        if nxt <= num:
            cnt += 1
            cur = num
            nxt = cur + mid
    return cnt


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    nums = []
    for _ in range(N):
        nums.append(int(input()))
    nums.sort()

    l = 1
    r = 1000000001
    mid_save = mid = (l + r) // 2
    while l <= r:
        if install_router(mid) >= M:
            mid_save = mid
            l = mid + 1
            mid = (l + r) // 2
        else:
            r = mid - 1
            mid = (l + r) // 2

    print(mid_save)