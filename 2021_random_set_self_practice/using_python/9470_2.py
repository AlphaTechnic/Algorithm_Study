"""
input :
1
1 7 8
1 3
2 3
6 4
3 4
3 5
6 7
5 7
4 7

output :
1 3
"""
import sys
from collections import defaultdict
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def topological_sort():
    # initialize
    que = deque([nd for nd, dg in enumerate(indeg[1:], start=1) if dg == 0])
    value = [0 for _ in range(V + 1)]
    for nd in que:
        value[nd] = 1
    parmxv = [0 for _ in range(V + 1)]
    mxvcnt = [0 for _ in range(V + 1)]

    MXV = 1
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if parmxv[nxt] < value[cur]:  # 갱신
                parmxv[nxt] = value[cur]
                mxvcnt[nxt] = 1
                value[nxt] = value[cur]
            elif parmxv[nxt] == value[cur]:  # mxv 재등장
                mxvcnt[nxt] += 1
                if mxvcnt[nxt] >= 2:
                    value[nxt] = value[cur] + 1

            MXV = max(MXV, value[nxt])

            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                que.append(nxt)

    return MXV


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        Q, V, E = map(int, input().rstrip().split())
        graph = defaultdict(list)
        indeg = [0 for _ in range(V + 1)]
        for _ in range(E):
            a, b = map(int, input().rstrip().split())
            graph[a].append(b)
            indeg[b] += 1

        print(Q, topological_sort())
