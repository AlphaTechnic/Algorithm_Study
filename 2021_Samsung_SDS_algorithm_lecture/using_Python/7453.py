"""
input :
6
-45 22 42 -16
-41 -27 56 30
-36 53 -37 77
-36 30 -75 -46
26 -38 -10 62
-32 -54 -6 45

output :
5
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
A = []
B = []
C = []
D = []
CD = dict()
for _ in range(N):
    a, b, c, d = map(int, input().rstrip().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for i in range(N):
    for j in range(N):
        if C[i] + D[j] in CD:
            CD[C[i] + D[j]] += 1
        else:
            CD[C[i] + D[j]] = 1


tot = 0
for i in range(N):
    for j in range(N):
        T = -(A[i] + B[j])
        if T in CD:
            tot += CD[T]
print(tot)
