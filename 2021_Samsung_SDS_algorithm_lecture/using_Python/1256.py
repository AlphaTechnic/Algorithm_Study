"""
input :
2 2 2

output :
azaz
"""

INF = 1000000010

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


cache = [[-1 for _ in range(101)] for _ in range(101)]
ans = ""


def get_az(A, Z):
    if A == 0 or Z == 0: return 1;

    if cache[A][Z] != -1: return cache[A][Z]

    cache[A][Z] = get_az(A - 1, Z) + get_az(A, Z - 1)
    if cache[A][Z] >= INF: cache[A][Z] = INF

    return cache[A][Z]


if __name__ == "__main__":
    A, Z, K = map(int, input().rstrip().split())
    if get_az(A, Z) < K:
        print(-1)
        exit()

    # 가장 앞에 있는 문자부터 채워나감
    tot = 0
    cntA = A
    cntZ = Z
    for i in range(A + Z):
        if cntA >= 1:
            tmp = get_az(cntA - 1, cntZ)  # a가 왔을 때 경우의 수
            if tot + tmp < K:
                ans += 'z'
                cntZ -= 1

                tot += tmp
            else:
                ans += 'a'
                cntA -= 1

        else:
            ans += 'z'

    print(ans)