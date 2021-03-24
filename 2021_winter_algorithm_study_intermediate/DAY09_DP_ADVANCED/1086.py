import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline


def gcd(p, q):
    if q == 0:
        return p
    else:
        return gcd(q, p % q)


data = [0 for _ in range(20)]
pos = [0 for _ in range(20)]
dp = [[0 for _ in range(101)] for _ in range(1<<16)]

N = int(input())
a = []
for i in range(N):
    a.append(input())
K = int(input())

for i in range(N):
    data[i] = 0
    for t in a[i]:
        data[i] = ((data[i] * 10 % K) + ord(t) - ord('0')) % K
    data[i] %= K

    pos[i] = 1
    for _ in range(len(a[i])):
        pos[i] *= 10
        pos[i] %= K

dp[0][0] = 1

for i in range(1<<N):
    for j in range(N):
        if (i & (1 << j)) == 0:
            for q in range(K):
                dp[i | (1<<j)][(q * pos[j] + data[j]) % K] += dp[i][q]

p = 1
for i in range(1, N+1):
    p *= i
g = gcd(dp[(1 << N) - 1][0], p)

upper = dp[(1 << N) - 1][0] // g
lower = p // g

if upper == 0:
    print('0/1')
elif upper == lower:
    print('1/1')
else:
    print(upper, end='')
    print('/', end='')
    print(lower)