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


def bfs(ss):
    que = deque(ss)
    value = [0 for _ in range(V + 1)]
    for s in ss:
        value[s] = 1

    mxv = 1
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if value[nxt] > value[cur]: continue

            if value[nxt] < value[cur]:  # 새로운 mxv가 나오면 갱신
                value[nxt] = value[cur]
                que.append(nxt)
            elif value[nxt] == value[cur]:  # mxv가 재등장한거면, nxt는 숫자 하나 키움
                value[nxt] = value[cur] + 1
            mxv = max(mxv, value[nxt])
    return mxv


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

        ss = [nd for nd, dg in enumerate(indeg[1:], start=1) if dg == 0]
        print(Q, bfs(ss))
