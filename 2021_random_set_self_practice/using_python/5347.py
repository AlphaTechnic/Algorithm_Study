"""
input :
3
15 21
33 22
9 10

output :
105
66
90
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().rstrip().split())
        G = gcd(A, B)
        a = A // G
        b = B // G
        print(G * a * b)
