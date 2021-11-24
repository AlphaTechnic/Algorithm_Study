"""
input :
4 3
1 3
2 3
4 2

output :
0 1
1 1
3 0
0 2
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = int(1e4)

if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    dist_par = [[INF for _ in range(V + 1)] for _ in range(V + 1)]
    dist_chd = [[INF for _ in range(V + 1)] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        dist_par[b][a] = 1
        dist_chd[a][b] = 1

    for k in range(1, V + 1):
        for a in range(1, V + 1):
            for b in range(1, V + 1):
                dist_par[a][b] = min(dist_par[a][b], dist_par[a][k] + dist_par[k][b])
                dist_chd[a][b] = min(dist_chd[a][b], dist_chd[a][k] + dist_chd[k][b])

    for v in range(1, V + 1):
        print(len(list(filter(lambda x: 0 < x < INF, dist_par[v]))), end=' ')
        print(len(list(filter(lambda x: 0 < x < INF, dist_chd[v]))), end=' ')
        print()
