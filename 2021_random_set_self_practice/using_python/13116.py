"""
input :
3
33 79
9 15
1022 1023

output :
40
10
5110
"""
import sys
import math
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


LOG = 10


def LCA(a, b):
    # 무조거 a를 더 깊게
    if a < b:
        a, b = b, a

    # a와 b의 레벨을 같게
    depa = int(math.log(a, 2))
    depb = int(math.log(b, 2))
    dep_diff = depa - depb
    for i in range(LOG, -1, -1):
        if dep_diff & (1 << i) == (1 << i):
            a //= (2 ** (1 << i))

    # 만약, a가 b에 도달을 해보렸다면? => return
    if a == b: return a

    # 그렇지 않다면, 같이 jump jump해서 위로 올라감
    for i in range(LOG, -1, -1):
        if (a >> 1) != (b >> 1):
            a >>= 1
            b >>= 1

    return a >> 1


if __name__ == "__main__":
    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().rstrip().split())
        print(10 * LCA(a, b))
