"""
input :
3
2 3000
5 5000
7 2000

output :
2 3 1
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def comp(arr):
    p = arr[1]
    w = arr[0]
    return (10000 - p) / w, arr[2]


if __name__ == "__main__":
    N = int(input())
    prices = []
    for i in range(N):
        price, p = map(int, input().rstrip().split())
        prices.append([price, p, i + 1])

    prices.sort(key=lambda x: comp(x))

    for _, _, ind in prices:
        print(ind, end=' ')
    print()
