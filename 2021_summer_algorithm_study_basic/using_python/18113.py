"""
input :
3 6 4
20
10
3

output :
2
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = 10 ** 9 + 3


def remove_ggodari():
    for i in range(len(gimbobs)):
        if gimbobs[i] >= 2 * K:
            gimbobs[i] -= 2 * K
        elif gimbobs[i] > K:
            gimbobs[i] -= K
        else:
            gimbobs[i] = 0


def cut_gimbob(mid):
    global M
    tot = 0
    for gimbob in gimbobs:
        tot += gimbob // mid

    if tot >= M:
        return True
    else:
        return False


if __name__ == "__main__":
    N, K, M = map(int, input().rstrip().split())
    gimbobs = []
    for _ in range(N):
        gimbobs.append(int(input()))

    remove_ggodari()

    l = 1
    r = INF
    mid = (l + r) // 2
    while l <= r:
        if cut_gimbob(mid):
            mid_save = mid
            l = mid + 1
            mid = (l + r) // 2
        else:
            r = mid - 1
            mid = (l + r) // 2

    try:
        print(mid_save)
    except:
        print(-1)
