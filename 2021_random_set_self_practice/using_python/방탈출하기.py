"""
input :
6
5 -7 6 9 0 -3
3
9 -9 6

output :
1
0
1
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = set(map(int, input().rstrip().split()))

    Q = int(input())
    qs = list(map(int, input().rstrip().split()))
    for q in qs:
        print(1) if q in nums else print(0)
