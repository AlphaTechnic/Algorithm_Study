"""
input :
6
3 2
1
2
4
6
6
6
8

output :
YES
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
attack_possible_range, attack = map(int, input().split())
bomb_num = int(input())
zombies = ['_'] + [int(input()) for _ in range(N)]


def can_survive():
    global bomb_num
    bomb_range_que = deque()
    for i in range(1, N + 1):
        if len(bomb_range_que) != 0 and bomb_range_que[0] < i:
            bomb_range_que.popleft()
        if i <= attack_possible_range:
            zombies[i] -= attack * (i - len(bomb_range_que))
        else:
            zombies[i] -= attack * (attack_possible_range - len(bomb_range_que))

        if zombies[i] > 0:
            if bomb_num > 0:
                zombies[i] = 0
                bomb_range_que.append(i + attack_possible_range - 1)
                bomb_num -= 1
            else:
                return False
    return True


if can_survive():
    print("YES")
else:
    print("NO")
