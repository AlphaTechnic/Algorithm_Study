"""
input :
10 3
ABCCCBBAAA

output :
CLEAR!
"""
import sys
from dataclasses import dataclass

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


@dataclass
class Char:
    ch: chr
    cnt: int


def print_stk(stk):
    if not stk:
        print("CLEAR!")
        return

    for i in range(len(stk)):
        for _ in range(stk[i].cnt):
            print(stk[i].ch, end='')
    return


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    txt = list(input().rstrip())

    stk = []

    for ch in txt:
        if len(stk) == 0:
            stk.append(Char(ch, 1))
        elif stk[-1].ch == ch:
            stk[-1].cnt += 1
        else:
            if stk[-1].cnt >= M:
                stk.pop()
                if len(stk) != 0 and stk[-1].ch == ch:
                    stk[-1].cnt += 1
                    continue
            stk.append(Char(ch, 1))

    if len(stk) != 0 and stk[-1].cnt >= M:
        stk.pop()

    print_stk(stk)
