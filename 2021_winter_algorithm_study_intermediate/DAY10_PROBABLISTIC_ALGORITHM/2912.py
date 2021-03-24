import sys
import collections
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N, C = map(int, input().split())
colors = [0] + list(map(int, input().split()))
M = int(input())

for _ in range(M):
    s, e = map(int, input().split())

    hat = [0 for _ in range(C+1)]
    #print(collections.Counter(colors[s:e+1]).most_common(1))

    [(num, cnt)] = collections.Counter(colors[s:e + 1]).most_common(1)
    if cnt > (e-s+1) / 2:
        print("yes", num)
    else:
        print("no")
    # for i in range(s, e+1):
    #     ind = colors[i]
    #     hat[ind] += 1
    #
    #     if hat[ind] > (e-s+1) / 2:
    #         print("yes", ind)
    #         break
    # else:
    #     print("no")
