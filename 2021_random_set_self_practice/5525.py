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


def count_matches(text, pat):
    cnt = 0

    l = 0
    r = len(pat)
    while r <= len(text):
        if pat == text[l:r]:
            cnt += 1
            l += 1
            r += 1
        l += 1
        r += 1
    return cnt


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    text = list(input().rstrip())

    pat = make_pat(N)
    print(count_matches(text, pat))
