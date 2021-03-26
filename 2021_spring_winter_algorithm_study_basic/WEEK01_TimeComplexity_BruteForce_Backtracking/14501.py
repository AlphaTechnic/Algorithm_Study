"""
input :
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
T_list = []
P_list = []
for _ in range(N):
    T, P = map(int, input().split())
    T_list.append(T)
    P_list.append(P)


max_val = 0
def get_max_profit(day, profit):
    global max_val
    if day >= N:
        max_val = max(max_val, profit)
        return

    if day + T_list[day] <= N:
        get_max_profit(day + T_list[day], profit + P_list[day])
    get_max_profit(day + 1, profit)  # 상담하지 않고 다음 날로 진행


get_max_profit(0, 0)
print(max_val)
