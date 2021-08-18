"""
input :
1 1 5 5
3 3 5 5

output :
1
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def ccw(vec1, vec2):
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]


def disjoint(a, b, c, d):
    return max(a, b) < min(c, d) or min(a, b) > max(c, d)


if __name__ == "__main__":
    a, b, c, d = map(int, input().rstrip().split())
    e, f, g, h = map(int, input().rstrip().split())

    A = [a, b]; B = [c, d]; C = [e, f]; D = [g, h]

    AB = [c - a, d - b]; AC = [e - a, f - b]; AD = [g - a, h - b]
    CA = [e - a, f - b]; CB = [e - c, f - d]; CD = [g - e, h - f]

    res1 = ccw(AB, AC); res2 = ccw(AB, AD)
    res3 = ccw(CD, CA); res4 = ccw(CD, CB)

    if res1 * res2 == 0 and res3 * res4 == 0:
        if not disjoint(A[0], B[0], C[0], D[0]) and not disjoint(A[1], B[1], C[1], D[1]):
            print(1)
        else:
            print(0)
        exit()

    if res1 * res2 <= 0 and res3 * res4 <= 0:
        print(1)
    else:
        print(0)
