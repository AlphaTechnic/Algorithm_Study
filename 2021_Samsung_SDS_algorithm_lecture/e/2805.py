"""
input :
4 7
20 15 10 17

output :
15
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))

s = 0
e = max(trees)


def try_cutting(mid):
    tot = 0
    for tree in trees:
        tot += max(tree - mid, 0)

    return tot


if __name__ == "__main__":
    while s <= e:
        mid = (s + e) // 2

        # cut and get tot
        tot = try_cutting(mid)

        if tot < K:
            e = mid - 1
        else:  # tot >= K:
            ans = mid
            s = mid + 1

    print(ans)
