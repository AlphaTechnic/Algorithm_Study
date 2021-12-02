"""
input :
7
2 5 -3 1 3 -4 4

output :
2
"""
import sys
from collections import Counter

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def make_cum_sum(arr):
    cum_sum = [0]
    tot = 0
    for val in arr:
        tot += val
        cum_sum.append(tot)

    return cum_sum


def nC2(n):
    return (n * (n - 1)) // 2


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().rstrip().split()))

    cum_sum = make_cum_sum(arr)
    tot = 0
    for val, cnt in Counter(cum_sum).most_common():
        if cnt >= 2:
            tot += nC2(cnt)
    print(tot)
