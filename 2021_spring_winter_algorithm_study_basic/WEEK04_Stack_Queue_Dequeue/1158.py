"""
input :
7 3

output :
<3, 6, 2, 7, 5, 1, 4>
"""

import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())

nums = deque([i for i in range(1, N + 1)])

ans = "<"
while True:
    nums.rotate(-K + 1)
    if len(nums) == 0:
        break
    ans += str(nums.popleft()) + ", "
ans = ans[:-2] + ">"

print(ans)
