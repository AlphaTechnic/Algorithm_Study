"""
input :
5 76
5 4
36 25 1 36 36
4 4
30 24 25 20
6 4
36 36 36 36 36 36
2 4
3 7
5 4
27 15 26 8 14

output :
4
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())

    res = []
    for _ in range(N):
        candi_num, C = map(int, input().rstrip().split())
        ans_idx = candi_num - C

        candis = list(map(int, input().rstrip().split()))
        candis.sort()
        ans = candis[ans_idx] if ans_idx >= 0 else 1
        res.append(ans)

    res.sort()
    cnt = 0
    for i in range(len(res)):
        K -= res[i]
        if K < 0:
            break
        else:
            cnt += 1

    print(cnt)
