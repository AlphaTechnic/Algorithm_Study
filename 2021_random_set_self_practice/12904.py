"""
input :
B
ABBA

output :
1
"""
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def TAR_to_S(text):
    global S
    while True:
        if text == S:
            return True
        elif len(text) == len(S):
            return False

        if text[-1] == 'A':
            text.pop()
        elif text[-1] == 'B':
            text.pop()
            text.reverse()


if __name__ == "__main__":
    S = deque(input().rstrip())
    TAR = deque(input().rstrip())

    if TAR_to_S(TAR):
        print(1)
    else:
        print(0)
