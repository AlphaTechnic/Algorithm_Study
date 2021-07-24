"""
input :
10 12
1 2
2 2
1 2
2 3
3 1
2 2
2 5
2 1
5 1
2 3

output :
do
"""

import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def do_open():
    num = do_cards.pop()
    if len(do_cards) == 0: print("su"); exit()
    do_ground.append(num)
    return num


def su_open():
    num = su_cards.pop()
    if len(su_cards) == 0: print("do"); exit()
    su_ground.append(num)
    return num


def do_ring():
    while len(su_ground) != 0:
        num = su_ground.popleft()
        do_cards.appendleft(num)
    while len(do_ground) != 0:
        num = do_ground.popleft()
        do_cards.appendleft(num)


def su_ring():
    while len(do_ground) != 0:
        num = do_ground.popleft()
        su_cards.appendleft(num)
    while len(su_ground) != 0:
        num = su_ground.popleft()
        su_cards.appendleft(num)


def init_ds():
    global s
    global d
    s = -1; d = -1;


if __name__ == "__main__":
    CARD_NUM, GAME_NUM = map(int, input().rstrip().split())
    do_cards = deque()
    su_cards = deque()
    do_ground = deque()
    su_ground = deque()
    for _ in range(CARD_NUM):
        a, b = map(int, input().rstrip().split())
        do_cards.append(a)
        su_cards.append(b)

    init_ds()
    while True:
        d = do_open()
        if d == 5:
            do_ring()
            init_ds()
        elif d + s == 5:
            su_ring()
            init_ds()

        GAME_NUM -= 1
        if GAME_NUM == 0: break

        s = su_open()
        if s == 5:
            do_ring()
            init_ds()
        elif d + s == 5:
            su_ring()
            init_ds()

        GAME_NUM -= 1
        if GAME_NUM == 0: break

    if len(do_cards) > len(su_cards):
        print("do")
    elif len(do_cards) == len(su_cards):
        print("dosu")
    else:
        print("su")
