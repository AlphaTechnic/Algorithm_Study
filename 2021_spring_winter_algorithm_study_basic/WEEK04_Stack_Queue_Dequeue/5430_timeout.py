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
    funcs = funcs.replace("RR", "")
    SIZE = int(input())
    tmp = input().rstrip()
    if tmp != "[]":
        arr = deque(map(int, tmp.rstrip()[1:-1].split(",")))
    else:
        arr = []
    for func in funcs:
        if func == "R":
            arr.reverse()
        elif func == "D":
            if len(arr) != 0:
                arr.popleft()
            else:
                print("error")
                err_flag = 1

    if not err_flag:
        arr_str = list(map(str, arr))
        ans = ",".join(arr_str)
        print("[" + ans + "]")
