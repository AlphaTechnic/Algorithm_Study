import sys
sys.stdin = open("input.txt", "r")

import collections

N = int(input())
adj = [set() for _ in range(N+1)]
rumored = [set() for _ in range(N + 1)]
time = [-1 for _ in range(N+1)]

for ind in range(1, N+1):
    adj[ind] = set(map(int, input().split()[:-1]))

M = int(input())
queue = collections.deque([*map(int, input().split())])
for ind in queue:
    time[ind] = 0

for cur_time in range(1, N+3):
    len_of_queue = len(queue)
    while len_of_queue:
        len_of_queue -= 1
        cur = queue.popleft()
        for nxt in adj[cur]:
            if time[nxt] != -1:
                continue
            if cur not in rumored[nxt]:
                rumored[nxt].add(cur)
            if len(rumored[nxt]) * 2 >= len(adj[nxt]):
                time[nxt] = cur_time
                queue.append(nxt)

    if not queue:
        break

for i in time[1:]:
    print(i, end=' ')

