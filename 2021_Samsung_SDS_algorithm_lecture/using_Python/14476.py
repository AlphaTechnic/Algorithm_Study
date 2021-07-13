"""
input :
5
8 12 24 36 48

output :
12 8
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


N = int(input())
nums = [0] + list(map(int, input().rstrip().split())) + [0]

# 누적 gcd(?)를 미리 전처리한다.
left_gcds = [0 for _ in range(N + 2)]
right_gcds = [0 for _ in range(N + 2)]

for i in range(1, N + 1):
    left_gcds[i] = gcd(left_gcds[i - 1], nums[i])
for i in range(N, 0, -1):
    right_gcds[i] = gcd(right_gcds[i + 1], nums[i])

max_val = -1
who = -1
for i in range(1, N + 1):
    # nums[i]를 제외시킴
    tmp = gcd(left_gcds[i - 1], right_gcds[i + 1])

    if tmp > max_val and nums[i] % tmp != 0:
        max_val = tmp
        who = nums[i]

if max_val == -1:
    print(-1)
else:
    print(max_val, who)
