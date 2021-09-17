"""
input :
3
0 10
33 1005
1 4

output :
2
199
0
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())

    # 전처리
    cnt = [0 for _ in range(1000001)]
    for i in range(0, 1000001):
        str_i = str(i)
        for j in str_i:
            if j == '0':
                cnt[i] += 1

    for _ in range(T):
        N, M = map(int, input().rstrip().split())
        print(sum(cnt[N: M + 1]))
