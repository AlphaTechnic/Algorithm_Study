"""
input :
4 3

output :
1+2+1
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(num):
    global N

    if num == N:
        ans_case = [str(ele) for ele in tmp]
        ans.append(ans_case)
        return
    if num > N:
        return

    for i in [1, 2, 3]:
        tmp.append(i)
        recur(num + i)
        tmp.pop()


if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())

    ans = list()

    tmp = list()
    recur(0)

    ans.sort()
    if len(ans) >= K:
        print('+'.join(ans[K - 1]))
    else:
        print(-1)
