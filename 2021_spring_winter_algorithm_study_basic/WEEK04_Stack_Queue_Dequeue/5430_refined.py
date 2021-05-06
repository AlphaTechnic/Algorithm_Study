"""
input :
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]

output :
[2,1]
error
[1,2,3,5,8]
error
"""
import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    err_flag = 0

    funcs = input().rstrip()

    SIZE = int(input())
    tmp = input().rstrip()
    if tmp != "[]":
        arr = deque(map(int, tmp.rstrip()[1:-1].split(",")))
    else:
        arr = deque([])

    # 1 means 리버스 짝수회차 (-> drop이 나오면 왼쪽에서)
    # -1 means 리버스 홀수회차 (-> drop이 나오 오른쪽에서)
    R_flag = 1
    for func in funcs:
        if func == 'R':
            R_flag *= -1
        elif func == 'D':
            if R_flag == 1:
                if len(arr) != 0:
                    arr.popleft()
                else:
                    err_flag = 1
                    break
            if R_flag == -1:
                if len(arr) != 0:
                    arr.pop()
                else:
                    err_flag = 1
                    break
    if R_flag == -1 and not err_flag:
        arr.reverse()

    if not err_flag:
        arr_str = list(map(str, arr))
        ans = ",".join(arr_str)
        print("[" + ans + "]")
    else:
        print("error")
