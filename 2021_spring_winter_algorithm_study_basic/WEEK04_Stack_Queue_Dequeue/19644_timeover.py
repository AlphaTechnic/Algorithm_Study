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
zombies = deque([int(input()) for _ in range(N)])


def can_alive():
    global bomb_num
    for _ in range(N):
        # 맨 앞의 좀비 기관총 공격해봄
        zombies[0] -= attack

        end = min(attack_possible_range, len(zombies))
        if zombies[0] <= 0:  # 기관총 공격에 맨 앞 좀비 die라면, 유효 사거리 안의 나머지 좀비도 P 깎음
            for i in range(1, end):
                zombies[i] -= attack

        # 맨 앞 좀비 기관총으로 무찌를 수 없다면, 지뢰 사용
        else:
            if bomb_num > 0:
                bomb_num -= 1
            else:
                # 기관총까지도 안먹히면 사망
                return False

        # 좀비들 전진
        zombies.popleft()
    return True


if can_alive():
    print("YES")
else:
    print("NO")
