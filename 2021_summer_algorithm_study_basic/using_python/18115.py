"""
input :
5
1 1 1 1 1

output :
5 4 3 2 1
"""

import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def action1():
    num = ground.popleft()
    card_deq.appendleft(num)


def action2():
    num1 = ground.popleft()
    num2 = card_deq.popleft()
    card_deq.appendleft(num1)
    card_deq.appendleft(num2)


def action3():
    num = ground.popleft()
    card_deq.append(num)


if __name__ == "__main__":
    N = int(input())
    #  위 -> 아래

    ground = deque([i for i in range(1, N + 1)])
    card_deq = deque()
    action_dic = {1: action1, 2: action2, 3: action3}
    actions = list(map(int, input().rstrip().split()))
    for action in reversed(actions):
        action_dic[action]()

    for num in card_deq:
        print(num, end=' ')
