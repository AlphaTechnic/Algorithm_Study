"""
input :
7 2 3
1 2
2 1
4 7

output :
1
1
4
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    V, K, Q = map(int, input().rstrip().split())

    if K == 1:
        for _ in range(Q):
            a, b = map(int, input().rstrip().split())
            print(abs(b - a))

    else:
        for _ in range(Q):
            a, b = map(int, input().rstrip().split())

            cnt = 0
            while a != b:
                if a > b:
                    a, b = b, a

                b = (b + (K - 2)) // K
                cnt += 1
            print(cnt)
