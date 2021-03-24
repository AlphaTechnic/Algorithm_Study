import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)

n = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(n - 1):
    parent, child, weight = list(map(int, sys.stdin.readline().split()))
    adj[parent].append([child, weight])
    adj[child].append([parent, weight])


def get_longest_path(here, visit):
    ret = 0
    vertex = here
    visit.append(here)

    for near, weight in adj[here]:
        if near in visit:
            continue
        next, v = get_longest_path(near, visit)
        if next + weight > ret:
            ret = next + weight
            vertex = v
    return ret, vertex


_, vertex = get_longest_path(1, [])
cost, _ = get_longest_path(vertex, [])

print(cost)