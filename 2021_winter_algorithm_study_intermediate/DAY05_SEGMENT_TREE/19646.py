import sys
sys.stdin = open("input.txt", "r")

N = int(input())
d = [0 for _ in range(4*N)]
e = [0] + list(map(int, input().split()))


def get(p, left, right):
    if left == right:
        d[p] = e[left]
        return d[p]
    d[p] = get(p * 2, left, (left + right) // 2) + get(p * 2 + 1, (left + right) // 2 + 1, right)
    return d[p]


def sol(p, left, right, v):
    if left == right:
        return left
    if d[p*2] < v:
        return sol(p * 2 + 1, (left + right) // 2 + 1, right, v - d[p * 2])
    return sol(p * 2, left, (left + right) // 2, v)


def update(p, left, right, x):
    if x < left or right < x:
        return d[p]
    if left == right:
        d[p] = 0
        return d[p]
    d[p] = update(p * 2, left, (left + right) // 2, x) + update(p * 2 + 1, (left + right) // 2 + 1, right, x)
    return d[p]


get(1, 1, N)
p = list(map(int, input().split()))

for i in range(N):
    p[i] = sol(1, 1, N, p[i])
    print(p[i], end=" ")
    update(1, 1, N, p[i])


