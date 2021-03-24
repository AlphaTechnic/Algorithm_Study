import sys
import random
sys.stdin = open("input.txt", "r")


def sum_vec(v, u):
    a = v[0] + u[0]
    b = v[1] + u[1]
    return [a, b]


def sub_vec(v, u):
    a = v[0] - u[0]
    b = v[1] - u[1]
    return [a, b]


def cross(v, u):
    return v[0]*u[1] - v[1]*u[0]


N = int(input())
p = int(input())

if N == 1:
    print("possible")

else:
    vec = []
    for i in range(N):
        x, y = map(int, input().split())
        vec.append([x, y])

    flag = False
    for _ in range(500):
        i = j = 0
        while i == j:
            i = random.randint(0, N-1)
            j = random.randint(0, N-1)

        line = 0
        for k in range(N):
            v1 = sub_vec(vec[i], vec[k])
            v2 = sub_vec(vec[j], vec[k])
            if cross(v1, v2) == 0:
                line += 1

        if line*100 >= p*N:
            flag = True
            break

    if flag:
        print("possible")
    else:
        print("impossible")

