"""
input :
5
25 3 4
4 4 6
9 2 3
16 2 5
1 5 2

output :
3
5
3
1
"""
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


class P:
    def __init__(self, idx, area, value, weight):
        self.idx = idx
        self.area = area
        self.value = value
        self.weight = weight


if __name__ == "__main__":
    N = int(input())

    data = []
    for i in range(1, N + 1):
        area, value, weight = map(int, input().rstrip().split())
        obj = P(i, area, value, weight)
        data.append(obj)
    data.sort(key=lambda x: (-x.area, -x.weight))

    data = [P(0, 10 ** 9, 0, 10 ** 9)] + data
    # for d in data:
    #     print(d.idx, d.area, d.value, d.weight)

    par = [0 for _ in range(N + 1)]
    dp = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(i):
            if data[i].weight <= data[j].weight and dp[i] < dp[j] + data[i].value:
                dp[i] = dp[j] + data[i].value
                par[i] = j

    res = []
    mxv = max(dp)
    i = dp.index(mxv)
    while True:
        if par[i] == 0:
            res.append(data[i].idx)
            break
        else:
            res.append(data[i].idx)
            i = par[i]

    print(len(res))
    print('\n'.join(map(str, res)))


