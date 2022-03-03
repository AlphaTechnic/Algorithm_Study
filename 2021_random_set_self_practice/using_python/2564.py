import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dist(t1, coord1, t2, coord2):
    if t1 > t2:
        t1, t2 = t2, t1
        coord1, coord2 = coord2, coord1

    # 같은 라인
    if t1 == t2:
        return abs(coord1 - coord2)

    # 평행하게
    if (t1, t2) == (3, 4):
        return min(coord1 + coord2, 2 * H - coord1 - coord2) + W
    if (t1, t2) == (1, 2):
        return min(coord1 + coord2, 2 * W - coord1 - coord2) + H

    # 직각인 경우
    if (t1, t2) == (1, 4):
        return W - coord1 + coord2
    if (t1, t2) == (1, 3):
        return coord1 + coord2
    if (t1, t2) == (2, 3):
        return coord1 + H - coord2
    if (t1, t2) == (2, 4):
        return W - coord1 + H - coord2


if __name__ == "__main__":
    W, H = map(int, input().rstrip().split())
    N = int(input())

    dots = []
    for _ in range(N):
        t, coord = map(int, input().rstrip().split())
        dots.append((t, coord))

    origin_t, origin_coord = map(int, input().rstrip().split())
    tot = 0
    for t, coord in dots:
        tot += dist(origin_t, origin_coord, t, coord)
    print(tot)
