"""
input:
210

output:
105
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N_str = input()
N = int(N_str)
if N <= 99:
    print(N)
elif 100 <= N <= 110:
    print(99)
elif 110 < N <= 999:
    cnt = 99
    num = 111
    num_str = str(111)
    while num <= N:
        num_list = list(map(int, num_str))
        dx1 = num_list[1] - num_list[0]
        dx2 = num_list[2] - num_list[1]
        if dx1 == dx2:
            cnt += 1

        num += 1
        num_str = str(num)
    print(cnt)

else: # N == 1000
    print(144)