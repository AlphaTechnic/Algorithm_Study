import sys

sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10000)


def gcd(A, B):
    if B == 0:
        return A
    return gcd(B, A % B)


N, M = map(int, input().split(':'))
if M > N:
    N, M = M, N
    G = gcd(N, M)
    print("%s:%s" % (M // G, N // G))
else:
    G = gcd(N, M)
    print("%s:%s" % (N // G, M // G))
