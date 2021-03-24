import sys
sys.stdin = open("input.txt", "r")


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []

    for _ in range(M):
        a, b, w = map(int, input().split())
        edges.append((a, b, w))
        edges.append((b, a, w))
    for _ in range(W):
        a, b, w = map(int, input().split())
        edges.append((a, b, -w))

    dist = [0 for _ in range(N+1)]


    def bellmanford():
        for i in range(N+1):
            for edge in edges:
                cur, nxt, weight = edge
                if dist[nxt] > dist[cur] + weight:
                    dist[nxt] = dist[cur] + weight
                    if i == N:
                        return True
        return False

    if bellmanford():
        print("YES")
    else:
        print("NO")