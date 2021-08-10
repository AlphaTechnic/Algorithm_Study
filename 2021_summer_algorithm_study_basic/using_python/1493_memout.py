"""
input :
4 4 8
3
0 10
1 10
2 1

output :
9
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


class SZ2CNT:
    def __init__(self, sz, cnt):
        self.sz = sz
        self.cnt = cnt


def recur(L, W, H):
    global CUBE_NUM; global possible
    if not possible:
        return
    if L == 0 or W == 0 or H == 0:
        return

    for obj in sz2cnt:
        if not (obj.sz <= L and obj.sz <= W and obj.sz <= H): continue
        if obj.cnt <= 0: continue

        CUBE_NUM += 1; obj.cnt -= 1;

        recur(L, W, H - obj.sz)
        recur(obj.sz, W - obj.sz, obj.sz)
        recur(L - obj.sz, W, obj.sz)
        return
    possible = False


if __name__ == "__main__":
    L, W, H = map(int, input().rstrip().split())
    N = int(input())
    sz2cnt = []
    for _ in range(N):
        a, b = map(int, input().rstrip().split())
        obj = SZ2CNT(2 ** a, b)
        sz2cnt.append(obj)

    sz2cnt.sort(reverse=True, key=lambda x: x.sz)

    CUBE_NUM = 0
    possible = True
    recur(L, W, H)

    if possible:
        print(CUBE_NUM)
    else:
        print(-1)