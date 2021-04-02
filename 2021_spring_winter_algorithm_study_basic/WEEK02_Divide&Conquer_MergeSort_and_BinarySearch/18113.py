"""
input :
3 6 4
20
10
3
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K, M = map(int, input().split())
kimbab_list = []
for _ in range(N):
    kimbab_list.append(int(input()))

kimbab_refined_list = []
for kimbab in kimbab_list:
    if kimbab > 2*K:
        kimbab_refined_list.append(kimbab - 2 * K)
    elif K < kimbab < 2*K:
        kimbab_refined_list.append(kimbab - K)

total_of_kimbab = sum(kimbab_refined_list)
if total_of_kimbab < M:
    print(-1)
    exit()
elif total_of_kimbab == M:
    print(1)
    exit()

low = 1
high = max(kimbab_refined_list)
ans = 0
while low <= high:
    mid = (low + high) // 2
    total = 0
    for kimbab_refined in kimbab_refined_list:
        if kimbab_refined >= mid:
            total += kimbab_refined // mid

    if total >= M:
        ans = mid
        low = mid + 1
    elif total < M:
        high = mid - 1

print(ans)