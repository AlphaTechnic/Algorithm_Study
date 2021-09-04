"""
input :
3
4
7
10

output :
4
8
14
"""
import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def recur(num):
    global cnt

    if num == N:
        cnt += 1
        return
    if num > N:
        return

    for i in [1, 2, 3]:
        if len(tmp) != 0 and i < tmp[-1]: continue

        tmp.append(i)
        recur(num + i)
        tmp.pop()


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())

        cnt = 0
        tmp = list()
        recur(0)

        print(cnt)
