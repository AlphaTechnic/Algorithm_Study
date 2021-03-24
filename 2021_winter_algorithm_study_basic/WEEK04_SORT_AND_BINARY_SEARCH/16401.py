import sys
sys.stdin = open("input.txt", "r")

M, N = map(int, input().split())
length_list = list(map(int, input().split()))
length_list.sort()

low = 1
high = length_list[-1]
ans = 0
while low <= high:
    mid = (low + high) // 2
    sum = 0
    for length in length_list:
        sum += length // mid

    if sum < M:
        high = mid - 1
    else:
        ans = mid
        low = mid + 1

print(ans)