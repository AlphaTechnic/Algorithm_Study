"""
input :
4
1 4 13 40

output :
121
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def fun1():
    print('A')
    exit(0)


def fun2():
    if nums[0] != nums[1]:
        print('A')
    else:
        print(nums[1])
    exit(0)


def get_ab(x, y, z):
    if y - x == 0:
        if z - y == 0:
            return 1, 0
        else:
            print('B')
            exit(0)
    else:
        # a, b가 정수로 안 나오면 실패
        if (z - y) % (y - x) != 0:
            print('B')
            exit(0)

        a = (z - y) // (y - x)
        b = (y ** 2 - z * x) // (y - x)
        return a, b


if __name__ == "__main__":
    N = int(input())
    if N == 1:
        fun1()

    nums = list(map(int, input().rstrip().split()))
    if N == 2:
        fun2()

    # N >= 3
    x = nums[0]
    y = nums[1]
    z = nums[2]
    a, b = get_ab(x, y, z)

    for i in range(3, N):
        if a * nums[i - 1] + b != nums[i]:
            print('B')
            exit(0)
    print(a * nums[N - 1] + b)
