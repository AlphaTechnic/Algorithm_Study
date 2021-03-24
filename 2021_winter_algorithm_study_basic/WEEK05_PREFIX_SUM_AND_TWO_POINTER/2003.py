import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split()) # N개의 수로 된 수열, M은 수열의 i번째 수부터 j번째 수까지의 합
num_list = list(map(int, input().split()))
pre = [0]
Sum = 0
for num in num_list:
    Sum += num
    pre.append(Sum)

cnt = 0
a = b = 1
while b <= N:
    sum_of_intervals = pre[b] - pre[a-1]
    if sum_of_intervals < M:
        b += 1
    elif sum_of_intervals > M:
        a += 1
    else: # sum_of_intervals == M
        cnt += 1
        b += 1

print(cnt)