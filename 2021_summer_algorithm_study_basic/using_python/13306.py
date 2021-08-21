"""
input :
3 3
1
1
1 2 3
0 3
1 2 3
1 1 2
0 2

output :
YES
NO
YES
"""
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")
input = sys.stdin.readline


def find(x):
    if parent[x] == -1:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False

    if height[a] < height[b]:
        a, b = b, a
    parent[b] = a

    if height[a] == height[b]:
        height[a] += 1

    return True


if __name__ == "__main__":
    V, Q = map(int, input().rstrip().split())
    parent = [-1 for _ in range(V + 1)]
    height = [0 for _ in range(V + 1)]
    parent_cpy = [-1 for _ in range(V + 1)]
    for i in range(2, V + 1):
        p = int(input())
        parent_cpy[i] = p

    Qs = list()
    for _ in range((V - 1) + Q):
        cmd = list(map(int, input().rstrip().split()))
        Qs.append(cmd)

    # 쿼리를 뒤에서부터 보면서, tree를 구축
    anses = deque()
    for i in range((V - 1) + Q - 1, -1, -1):
        cmd = Qs[i]
        if cmd[0] == 0:
            a = cmd[1]
            union(a, parent_cpy[a])

        elif cmd[0] == 1:
            # 연결되있3?
            a = cmd[1]
            b = cmd[2]
            if find(a) == find(b):
                anses.appendleft(1)
            else:
                anses.appendleft(0)

    for ans in anses:
        if ans == 1:
            print("YES")
        else:
            print("NO")
