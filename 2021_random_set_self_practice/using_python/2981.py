"""
input :
3
6
34
38

output :
2 4
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


if __name__ == "__main__":
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    g = nums[1] - nums[0]
    for i in range(2, len(nums)):
        g = gcd(g, abs(nums[i] - nums[i - 1]))

    ans = {g}
    for i in range(2, int(g ** 0.5) + 1):
        if g % i == 0:
            ans.add(i)
            ans.add(g // i)
    print(' '.join(map(str, sorted(ans))))
