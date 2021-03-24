import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
from_to_list = []
for _ in range(M):
    from_to_list.append(list(map(int, input().split())))

pre = [0]
sum = 0
for num in num_list:
    sum += num
    pre.append(sum)

for start, end in from_to_list:
    print(pre[end] - pre[start-1])