import sys
sys.stdin = open("input.txt", "r")

import collections

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    importance_list = collections.deque(map(int, input().split()))
    chk_list = collections.deque([False for _ in range(N)])
    chk_list[M] = True
    cnt = 0
    while len(importance_list) != 0:
        if len(importance_list) >= 1:
            for importance in list(importance_list)[1:]:
                first = importance_list[0]
                if importance > first:
                     importance_list.rotate(-1)
                     chk_list.rotate(-1)
                     break
            else:
                cnt += 1
                importance_list.popleft()
                if chk_list[0]:  # == True
                    print(cnt)
                    break
                else:
                    chk_list.popleft()
