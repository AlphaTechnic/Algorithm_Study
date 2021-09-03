"""
input :
-13

output :
110111
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    deq = deque()
    while N != 0:
        if N % (-2) == 0:
            deq.appendleft(0)
            N //= (-2)
        else:
            deq.appendleft(1)
            N = N // (-2) + 1

    if len(deq) == 0:
        print(0)
    else:
        for binary in deq:
            print(binary, end='')
        print()
