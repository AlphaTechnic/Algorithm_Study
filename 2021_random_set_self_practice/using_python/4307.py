"""
input :
2
10 3
2
6
7
214 7
11
12
7
13
176
23
191

output :
4 8
38 207
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        L, N = map(int, input().rstrip().split())
        mxv_of_short = 0
        mxv_of_long = 0
        for _ in range(N):
            num = int(input())
            other = L - num
            if num > other:
                num, other = other, num  # num 이 short 파트
            mxv_of_short = max(mxv_of_short, num)
            mxv_of_long = max(mxv_of_long, other)
        print(mxv_of_short, mxv_of_long)
