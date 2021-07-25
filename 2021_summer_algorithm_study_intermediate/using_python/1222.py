"""
input :
5
4 6 3 8 9

output :
9
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    loop_cnt = max(nums)
    cnt = [0 for _ in range(loop_cnt + 1)]
    for num in nums:
        cnt[num] += 1

    ans = -1
    # 아래와 같은 loop의 시간복잡도는 NlogN이다.
    for i in range(1, loop_cnt + 1):
        participant_num = 0
        for j in range(i, loop_cnt + 1, i):
            participant_num += cnt[j]

        if participant_num >= 2:
            ans = max(ans, participant_num * i)
    print(ans)
