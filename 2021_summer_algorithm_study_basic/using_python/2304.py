"""
input :
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6

output :
98
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def get_area():
    tot = 0

    # left -> right
    max1 = 0
    x1 = 0
    for i in range(1001):
        if height[i] > max1:
            tot += max1 * (i - x1)
            max1 = height[i]
            x1 = i

    # right -> left
    max2 = 0
    x2 = 1000
    for i in range(1000, -1, -1):
        if height[i] > max2:
            tot += max2 * (x2 - i)
            max2 = height[i]
            x2 = i

    tot += max1 * (x2 - x1 + 1)
    return tot


if __name__ == "__main__":
    N = int(input())

    height = [0 for _ in range(1001)]
    for _ in range(N):
        a, b = map(int, input().rstrip().split())
        height[a] = b

    print(get_area())
