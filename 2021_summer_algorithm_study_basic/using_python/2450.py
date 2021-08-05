"""
input :
8
1 3 3 2 1 1 3 2

output :
2
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def comp123(x):
    if x == 1: return -1
    elif x == 2: return 0
    elif x == 3 : return 1


def comp132(x):
    if x == 1: return -1
    elif x == 2: return 1
    elif x == 3 : return 0


def comp213(x):
    if x == 1: return 0
    elif x == 2: return -1
    elif x == 3 : return 1


def comp231(x):
    if x == 1: return 1
    elif x == 2: return -1
    elif x == 3: return 0


def comp312(x):
    if x == 1: return 0
    elif x == 2: return 1
    elif x == 3: return -1


def comp321(x):
    if x == 1: return 1
    elif x == 2: return 0
    elif x == 3: return -1


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    min_val = 100000
    funs = [comp123, comp132, comp213, comp231, comp312, comp321]
    for fun in funs:
        sorted_nums = sorted(nums, key=lambda x: fun(x))

        chk = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(N):
            if nums[i] != sorted_nums[i]:
                chk[sorted_nums[i]][nums[i]] += 1

        tot = min(chk[1][2], chk[2][1]) + min(chk[1][3], chk[3][1]) + min(chk[2][3], chk[3][2])
        tot += (max(chk[1][2], chk[2][1]) - min(chk[1][2], chk[2][1])) * 2

        min_val = min(min_val, tot)

    print(min_val)
