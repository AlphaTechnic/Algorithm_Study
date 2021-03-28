"""
연산자 끼워 넣기
input :
6
1 2 3 4 5 6
2 1 1 1

output :
54
-24
"""

import sys

sys.setrecursionlimit(3000)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
four_opers = dict()
opers = ["+", "-", "*", "//"]
num_of_oper = list(map(int, input().split()))
for oper, num in zip(opers, num_of_oper):
    four_opers[oper] = num


max_val = -10 ** 10
min_val = 10 ** 10
val = num_list[0]
def find_max_and_min(lv):
    global max_val, min_val, val;
    if lv == N:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return

    for oper in four_opers:
        if four_opers[oper] == 0: continue

        if oper == '+':
            val = val + num_list[lv]
            four_opers[oper] -= 1
            find_max_and_min(lv + 1)  ###### 재귀
            val = val - num_list[lv]
            four_opers[oper] += 1
        elif oper == '-':
            val = val - num_list[lv]
            four_opers[oper] -= 1
            find_max_and_min(lv + 1)  ###### 재귀
            val = val + num_list[lv]
            four_opers[oper] += 1
        elif oper == '*':
            val = val * num_list[lv]
            four_opers[oper] -= 1
            find_max_and_min(lv + 1)  ###### 재귀
            val = val // num_list[lv]
            four_opers[oper] += 1
        else:  # oper == '//'
            tmp = val
            if val < 0:
                val = -val // num_list[lv]
                val *= -1
            else:
                val = val // num_list[lv]
            four_opers[oper] -= 1
            find_max_and_min(lv + 1)  ###### 재귀
            val = tmp
            four_opers[oper] += 1


find_max_and_min(1)
print(max_val)
print(min_val)
