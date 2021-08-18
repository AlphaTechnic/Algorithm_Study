"""
input :
2
1 1
1 99
99 99
99 1

output :
2
1
"""
import sys
from itertools import permutations, combinations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def ccw(A, B, C):
    return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])


def disjoint(a, b, c, d):
    return max(a, b) < min(c, d) or min(a, b) > max(c, d)


def intersect(p1, p2, q1, q2):
    AB2CD = ccw(p1, p2, q1) * ccw(p1, p2, q2)
    CD2AB = ccw(q1, q2, p1) * ccw(q1, q2, p2)
    if AB2CD == 0 and CD2AB == 0:
        return not disjoint(p1[0], p2[0], q1[0], q2[0]) and not disjoint(p1[1], p2[1], q1[1], q2[1])
    return AB2CD <= 0 and CD2AB <= 0


if __name__ == "__main__":
    N = int(input())
    robots = []
    for _ in range(N):
        a, b = map(int, input().rstrip().split())
        robots.append((a, b))

    targets = []
    pos2num = dict()
    for i in range(1, N + 1):
        a, b = map(int, input().rstrip().split())
        targets.append((a, b))
        pos2num[(a, b)] = i

    for permu in permutations(targets, len(targets)):
        lines = list(zip(robots, permu))
        for combi in combinations(lines, 2):
            p1, p2 = combi[0]
            q1, q2 = combi[1]
            if intersect(p1, p2, q1, q2):
                break
            else:
                pass
        else:
            for _, pos in lines:
                print(pos2num[pos])
            break
