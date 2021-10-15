"""
input :
6
10 20 10 30 20 50

output :
4
"""
import sys
from bisect import bisect_left

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def compress(nums):
    # 주어진 수들에 index를 붙이고, sort
    # index를 붙이는 이유는 문제에서 준 순서를 기억했다가 그대로 다시 원상복구하기 위함
    num2idx = []
    for idx, num in enumerate(nums):
        num2idx.append([num, idx])
    num2idx.sort()

    # 좌표 압축한 다음 리턴
    num2idx_v2 = [(1, num2idx[0][1])]
    order = 1
    for i, [num, idx] in enumerate(num2idx[1:], start=1):
        if num != num2idx[i - 1][0]:
            order += 1
        num2idx_v2.append((order, idx))
    num2idx_v2.sort(key=lambda x: x[1])
    return [a[0] for a in num2idx_v2]


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    nums_comp = compress(nums)
    seq = [nums_comp[0]]
    for num in nums_comp:
        if num > seq[-1]:
            seq.append(num)
        else:
            idx = bisect_left(seq, num)
            seq[idx] = num
    print(len(seq))
