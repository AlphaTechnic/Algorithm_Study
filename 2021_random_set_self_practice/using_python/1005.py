"""
input :
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7

output :
39
"""
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        V, E = map(int, input().rstrip().split())
        costs = ['_'] + list(map(int, input().rstrip().split()))
        graph = dict()
        for i in range(V + 1):
            graph[i] = list()

        indeg = [0 for _ in range(V + 1)]
        cumulative_costs = [ele for ele in costs]
        for _ in range(E):
            a, b = map(int, input().rstrip().split())
            graph[a].append(b)
            indeg[b] += 1
        TAR = int(input())

        # que에 첫빠따 담음
        que = deque()
        for i in range(1, V + 1):
            if indeg[i] == 0:
                que.append(i)

        # 위상정렬 하면서, node에 누적된 비용 기록
        while que:
            cur = que.popleft()
            for nxt in graph[cur]:
                cumulative_costs[nxt] = max(cumulative_costs[nxt], cumulative_costs[cur] + costs[nxt])
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    que.append(nxt)

        print(cumulative_costs[TAR])
