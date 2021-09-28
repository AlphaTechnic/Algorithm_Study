"""
input :
11

output:
m
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def mk_nth_len():
    # N번째 수열의 길이 구하기
    p = [3]

    ind = 0
    while True:
        p.append(2 * p[ind] + ind + 1 + 3)
        ind += 1
        if p[ind] >= 10 ** 9:
            break
    return p


def fnd_N(idx, p):
    # ?번째 수열에게 떤질 것인가
    for i in range(len(p)):
        if idx <= p[i]:
            break
    return i


def recur(idx, N, p):
    if N == 0:
        return 'm' if idx == 1 else 'o'

    t1 = (p[N] - (N + 3)) // 2
    t2 = t1 + N + 3

    if 1 <= idx <= t1:
        return recur(idx, N - 1, p)
    elif t1 + 1 <= idx <= t2:
        return 'm' if idx == t1 + 1 else 'o'
    else:
        return recur(idx - t2, N - 1, p)


if __name__ == "__main__":
    idx = int(input())
    nth_len = mk_nth_len()
    N = fnd_N(idx, nth_len)

    print(recur(idx, N, nth_len))
