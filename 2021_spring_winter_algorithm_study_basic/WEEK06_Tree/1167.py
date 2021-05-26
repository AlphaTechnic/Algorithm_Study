import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    info = list(map(int, input().rstrip().split()))
    ind = 1
    while True:
        if ind >= len(info)-1:
            break
        graph[info[0]].append(info[ind: ind+2])
        ind += 2

max_val = 0
tmp = 0
last_node = 0
def find_maxlen_by_dfs(cur_node):
    global max_val
    global tmp
    global last_node
    visited[cur_node] = True
    for node, length in graph[cur_node]:
        if not visited[node]:
            break
    else:
        if tmp > max_val:
            last_node = cur_node
            max_val = tmp
        return

    for nxt, length in graph[cur_node]:
        if not visited[nxt]:
            visited[nxt] = True
            tmp += length
            find_maxlen_by_dfs(nxt)
            tmp -= length

# 반드시 개입되어야 하는 last node 찾기
visited = [False for _ in range(N + 1)]
find_maxlen_by_dfs(1)

# 그 last node를 시작 노드로 해서 dfs 돌기
visited = [False for _ in range(N + 1)]
find_maxlen_by_dfs(last_node)

print(max_val)
