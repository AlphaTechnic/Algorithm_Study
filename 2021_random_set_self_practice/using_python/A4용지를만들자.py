"""
input :
50 60

output :
3
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(W, H):
    r = W // 20
    c, remain = divmod(H, 40)
    if c == 0:
        return 0

    if remain > W:
        remain, W = W, remain

    ans = r * c + recur(remain, W)
    return ans


if __name__ == "__main__":
    W, H = map(int, input().rstrip().split())
    if W > H:
        W, H = H, W
    print(recur(W, H))
