"""
input :
6 4
4 1
8

output :
0 1
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    W, H = map(int, input().rstrip().split())
    x, y = map(int, input().rstrip().split())
    T = int(input())

    nx = (T % (2 * W) + x) % (2 * W)
    if nx > W:
        nx = 2 * W - nx
    ny = (T % (2 * H) + y) % (2 * H)
    if ny > H:
        ny = 2 * H - ny
    print(nx, ny)
