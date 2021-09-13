"""
input :
3
0 3
1 5
45 50

output :
3
3
4
"""
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
MAX = (1 << 32) + 5


def binary_search(TAR):
    l = 0
    r = len(pre_data)
    mid = (l + r) // 2
    while l <= r:
        if TAR <= pre_data[mid][0]:
            r = mid - 1
            mid = (l + r) // 2
        else:
            l = mid + 1
            mid = (l + r) // 2
    return pre_data[mid][1]


if __name__ == "__main__":
    # 데이터 전처리
    pre_data = []  # interval, num
    interval = 1
    num = 1
    p = 1
    while interval < MAX:
        pre_data.append((interval, num))
        num += 1
        interval += p

        pre_data.append((interval, num))
        num += 1

        p += 1
        interval += p

    # 쿼리에 대응
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().rstrip().split())
        if b - a == 1:
            print(1)
            continue
        print(binary_search(b - a) + 1)
