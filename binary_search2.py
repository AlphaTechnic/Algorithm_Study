import sys
import bisect

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for obj in data:
        if obj > mid:
            total += obj - mid

    if total < M:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)