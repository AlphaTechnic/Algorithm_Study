"""
input :
4 2
1 5 2
3 7 4
7 9 1
10 13 4
1 3
1 4

output :
1
0
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


class Interval():
    def __init__(self, a, b, y, idx):
        self.a = a
        self.b = b
        self.y = y
        self.idx = idx


def find(x):
    if par[x] == -1:
        return x
    par[x] = find(par[x])
    return par[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b: return False

    if height[a] < height[b]:
        a, b = b, a
    par[b] = a

    if height[a] == height[b]:
        height[a] += 1
    return True


if __name__ == "__main__":
    N, Q = map(int, input().rstrip().split())

    interval = []
    for idx in range(1, N + 1):
        a, b, y = map(int, input().rstrip().split())
        interval.append(Interval(a, b, y, idx))
    interval.sort(key=lambda x: x.a)

    # for obj in interval:
    #     print(obj.a, obj.b, obj.idx)

    par = [-1 for _ in range(N + 1)]
    height = [0 for _ in range(N + 1)]

    i = 0
    j = 0
    while j < N:
        if interval[i].b >= interval[j].a:
            union(interval[i].idx, interval[j].idx)
            j += 1
        else:
            i += 1

    for _ in range(Q):
        a, b = map(int, input().rstrip().split())
        if find(a) == find(b):
            print(1)
        else:
            print(0)
