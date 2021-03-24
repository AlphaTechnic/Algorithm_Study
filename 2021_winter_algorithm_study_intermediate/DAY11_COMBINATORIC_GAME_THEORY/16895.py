import sys
sys.stdin = open("input.txt", "r")

N = int(input())
dummy = list(map(int, input().split()))
nim = 0
for i in dummy:
    nim ^= i

ans = 0
for i in range(N):
    for j in range(dummy[i]):
        if nim ^ dummy[i] ^ j == 0:
            ans += 1

print(ans)
