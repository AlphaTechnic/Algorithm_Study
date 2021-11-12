"""
input :
10 9
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9
1 10
2 3 10
1 4

output :
4
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find(a):
    if parent[a] == -1:
        return a
    parent[a] = find(parent[a])
    return parent[a]


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
    N, P = map(int, input().rstrip().split())
    tmans = list(map(int, input().rstrip().split()))
    tmans.pop(0)

    parent = [-1 for _ in range(N + 1)]
    height = [0 for _ in range(N + 1)]
    SZ = 1
    if len(tmans) >= 2:
        for i in range(1, len(tmans)):
            if union(tmans[i], tmans[i - 1]):
                SZ += 1
    elif len(tmans) == 0:
        print(P)
        exit(0)

    parties = []
    for _ in range(P):
        party = list(map(int, input().rstrip().split()))
        party.pop(0)
        parties.append(party)
    chk = [False for _ in range(P)]

    while True:
        sz_save = SZ
        for i, party in enumerate(parties):
            for mem in party:
                if find(mem) == find(tmans[0]):
                    for p in party:
                        if union(p, tmans[0]):
                            SZ += 1
                    chk[i] = True
                    break
        if sz_save == SZ:
            break

    cnt = 0
    for i in range(len(chk)):
        if not chk[i]:
            cnt += 1
    print(cnt)
