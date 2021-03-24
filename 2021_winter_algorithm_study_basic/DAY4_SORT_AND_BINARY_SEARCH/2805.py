import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
trees = list(map(int, input().split()))

high = max(trees)
low = 0
ans = 0
while high >= low:
    mid = int((high + low) / 2)
    sum = 0
    for height in trees:
        if height > mid:
            sum += height - mid

    # 아직 부족..
    if sum < M :
        high = mid - 1
    # 넉넉히 자름
    else:
        ans = mid
        low = mid + 1

print(ans)