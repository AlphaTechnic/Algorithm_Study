"""
input :
3 5
1 1
2 4

output :
14
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

MOD = 1000000007


# 빠른 제곱법
def fpow(a, n):
    ret = 1

    while n:
        if n & 1:
            ret = (ret * a) % MOD
        a = (a * a) % MOD  # a 사이즈 제곱씩 뻥튀기
        n >>= 1

    return ret


# 페르마의 소정리 이용
def combi(n, r):
    # get a = nPr, b = r!
    a = 1
    b = 1
    for i in range(r):
        a = a * (n - i) % MOD
        b = b * (r - i) % MOD

    return a * fpow(b, MOD - 2) % MOD  # b로 나눈다 = b의 역원을 곱한다 = b^(p-2)를 곱한다.


def how_many(sx, sy, tx, ty):
    x = tx - sx
    y = ty - sy
    return combi(x + y, x)


def AtoB(sx, sy, tx, ty, hx, hy):
    s_to_t = how_many(sx, sy, tx, ty)

    if sx <= hx <= tx and sy <= hy <= ty:
        s_to_hole = how_many(sx, sy, hx, hy)
        hole_to_dest = how_many(hx, hy, tx, ty)
        return s_to_t - s_to_hole * hole_to_dest
    else:
        return s_to_t


if __name__ == "__main__":
    X, Y = map(int, input().rstrip().split())
    acorn_x, acorn_y = map(int, input().rstrip().split())
    hole_x, hole_y = map(int, input().rstrip().split())

    a = AtoB(0, 0, acorn_x, acorn_y, hole_x, hole_y)
    b = AtoB(acorn_x, acorn_y, X, Y, hole_x, hole_y)
    print(a * b % MOD)
