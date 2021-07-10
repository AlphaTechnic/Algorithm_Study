"""
input :
14 5
1
3
4
2
2
4
3
4
3
3
3
2
3
3

output :
7 2
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, H = map(int, input().rstrip().split())
chk = [0 for _ in range(H + 1)]

for _ in range(N // 2):
    # 아래에서 올라오는 석순 정보
    num1 = int(input())
    chk[0] += 1
    chk[num1] += -1

    # 위에서 나오는 종유석 정보
    num2 = int(input())
    chk[H] += -1
    chk[H - num2] += 1

accumulated_sum = []
tot = 0
for num in chk:
    tot += num
    accumulated_sum.append(tot)

min_val = 200001
cnt = 0
for i in range(len(accumulated_sum) - 1):
    if accumulated_sum[i] < min_val:
        min_val = accumulated_sum[i]
        cnt = 1
    elif accumulated_sum[i] == min_val:
        cnt += 1

print(min_val, cnt)