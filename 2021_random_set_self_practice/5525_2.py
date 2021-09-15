"""
input :
1
13
OOIOIOIOIIOII

output :
4
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def make_pat(i):
    pat = list('I')
    while i != 0:
        pat.append('O')
        pat.append('I')
        i -= 1

    return pat


def count_matches(text, N):
    ans = 0

    cnt = 0
    i = 0
    while i < len(text):
        if text[i: i + 3] == ['I', 'O', 'I']:
            cnt += 1
            i += 2

            if cnt == N:
                ans += 1
                cnt -= 1

        else:
            cnt = 0
            i += 1

    return ans


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    text = list(input().rstrip())

    print(count_matches(text, N))
