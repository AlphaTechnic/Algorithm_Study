import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
INF = int(1e9)


def get_node_having_smallest_dist():
    min_val = INF
    node_having_min_dist = 0
    for node in range(1, V + 1):
        if distance[node] < min_val:
            if not visited[node]:
                min_val = distance[node]
                node_having_min_dist = node
    return node_having_min_dist


def dijkstra(start):
    # start 노드에 대해서 initialize
    distance[start] = 0
    visited[start] = True
    for node, weight in graph[start]:
        distance[node] = weight

    # 본격 반복문
    for _ in range(V-1):
        now = get_node_having_smallest_dist()
        visited[now] = True
        for nxt, weight in graph[now]:
            if distance[nxt] > distance[now] + weight:
                distance[nxt] = distance[now] + weight


V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]
distance = [INF for _ in range(V + 1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

dijkstra(start)

for i in range(1, V+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])

