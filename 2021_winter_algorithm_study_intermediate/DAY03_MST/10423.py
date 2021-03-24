import sys


def find(node):
    if node == list_parent[node][0]:
        return node
    list_parent[node][0] = find(list_parent[node][0])

    return list_parent[node][0]


def union(node1, node2, cost):
    global count, ans
    node1 = find(node1)
    node2 = find(node2)
    if node1 == node2 or (node1 in isConnected and node2 in isConnected):
        return
    ans += cost
    if node2 in isConnected:
        list_parent[node1][0] = list_parent[node2][0]
        if list_parent[node1][1]:
            list_parent[node2][1] += list_parent[node1][1]
            count += list_parent[node1][1]
            list_parent[node1][1] = 0

    elif node1 in isConnected:
        list_parent[node2][0] = list_parent[node1][0]
        if list_parent[node2][1]:
            list_parent[node1][1] += list_parent[node2][1]
            count += list_parent[node2][1]
            list_parent[node2][1] = 0

    if list_parent[node1][1] < list_parent[node2][1]:
        list_parent[node1][0] = list_parent[node2][0]

        if list_parent[node1][1]:
            list_parent[list_parent[node1][0]][1] += list_parent[node1][1]
            list_parent[node1][1] = 0

    else:
        list_parent[node2][0] = list_parent[node1][0]
        if list_parent[node2][1]:
            list_parent[list_parent[node2][0]][1] += list_parent[node2][1]
            list_parent[node2][1] = 0


N, M, K = map(int, sys.stdin.readline().split())
list_parent = [[i, 1] for i in range(N)]
isConnected = set()
list_edge = []
count = K
ans = 0
for city in list(map(int, sys.stdin.readline().split())):
    isConnected.add(city - 1)

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    list_edge.append([w, u - 1, v - 1])
list_edge.sort()
for edge in list_edge:
    union(edge[1], edge[2], edge[0])

    # print(list_parent)
    # print(count)
    if count >= N:
        break
print(ans)