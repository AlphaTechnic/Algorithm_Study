"""
input :
3
4 10 20 30 40
3 7 5 12
3 125 15 25

output :
70
3
35
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        nums = list(map(int, input().rstrip().split()))[1:]
        ans = list()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ans.append(gcd(nums[i], nums[j]))
        print(sum(ans))
