import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def mk_addr(category, disp):
    if category == 1:
        return disp
    if category == 2:
        return W + H + W - disp
    if category == 3:
        return 2 * (W + H) - disp
    if category == 4:
        return W + disp


def dist(origin, dot):
    len_of_square = 2 * (H + W)
    len_between = abs(origin - dot)
    return min(len_between, len_of_square - len_between)


if __name__ == "__main__":
    W, H = map(int, input().rstrip().split())
    N = int(input())

    dots = []
    for _ in range(N):
        category, disp = map(int, input().rstrip().split())
        dot = mk_addr(category, disp)
        dots.append(dot)
    category, disp = map(int, input().rstrip().split())
    origin = mk_addr(category, disp)

    tot = 0
    for dot in dots:
        tot += dist(origin, dot)
    print(tot)
