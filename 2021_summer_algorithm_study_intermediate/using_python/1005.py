"""
input :
2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
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
120
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
        graph = [[] for _ in range(V + 1)]
        indeg = [0 for _ in range(V + 1)]
        costs = [-1] + list(map(int, input().rstrip().split()))
        for _ in range(E):
            a, b = map(int, input().rstrip().split())
            graph[a].append(b)
            indeg[b] += 1
        TAR = int(input())

        # 각 노드에 이르는 최장길이를 기록
        dists = [-1] + [0 for _ in range(V)]
        que = deque()
        for i in range(1, V + 1):
            if indeg[i] == 0:
                que.append(i)
                dists[i] = costs[i]

        # 위상정렬 수행
        while len(que) != 0:
            cur = que.popleft()

            for nxt in graph[cur]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    que.append(nxt)

                dists[nxt] = max(dists[nxt], dists[cur] + costs[nxt])

        print(dists[TAR])
