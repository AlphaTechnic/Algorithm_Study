"""
input :
11

output :
m
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def recur(n):
    global a;
    if n == 0:
        return a
    text = recur(n - 1) + 'm' + 'o' * (n + 2) + recur(n - 1)
    return text


if __name__ == "__main__":
    N = int(input())
    a = "moo"
    print(recur(1 << 5)[N])