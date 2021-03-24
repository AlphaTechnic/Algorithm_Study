import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
T_list = []
for i in range(N):
    T_list.append(int(input()))

low = 1
high = max(T_list) * M

while low <= high:
    mid = (low+high) // 2
    sum = 0
    for T in T_list:
        sum += mid // T
        if sum > M:
            break

    if sum >= M:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)