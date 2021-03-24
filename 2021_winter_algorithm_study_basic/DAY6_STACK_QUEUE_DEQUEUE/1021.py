import sys
sys.stdin = open("input.txt", "r")

import collections


def left_machine(deque, target_num):
    cnt = 0
    while target_num != deque[0]:
        deque.rotate(-1)
        cnt += 1
    return cnt


def right_machine(deque, target_num):
    cnt = 0
    while target_num != deque[0]:
        deque.rotate(1)
        cnt += 1
    return cnt


def get_min_rotate(deque, target_num):
    deque_cpy = deque.copy()
    ans1 = left_machine(deque, target_num)
    ans2 = right_machine(deque_cpy, target_num)
    if ans1 > ans2:
        deque = deque_cpy
        ans1 = ans2
    return ans1, deque


N, M = map(int, input().split())
num_list = collections.deque([i for i in range(1, N+1)])
target_list = list(map(int, input().split()))

Sum = 0
for target in target_list:
    ans, num_list = get_min_rotate(num_list, target)
    num_list.popleft()
    Sum += ans

print(Sum)