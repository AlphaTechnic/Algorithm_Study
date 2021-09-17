"""
input :
2
2
0 0 1
1 0 1
3
0 0 1
2 0 1
10 0 5

output :
1
2
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
g_cnt = 0


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


def dist_square(pos1, pos2):
    return (pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        V = int(input())
        parent = [-1 for _ in range(V)]
        height = [0 for _ in range(V)]

        poses = list()
        for i in range(V):
            y, x, r = map(int, input().rstrip().split())
            poses.append((y, x, r))

        g_cnt = V
        for i in range(V):
            for j in range(i + 1, V):
                if dist_square(poses[i], poses[j]) <= (poses[i][2] + poses[j][2]) ** 2:
                    if union(i, j):
                        g_cnt -= 1
        print(g_cnt)
