"""
input :
1234567

output:
NO
3
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def sumup(txt):
    tot = 0
    for ch in txt:
        tot += int(ch)
    return str(tot)


if __name__ == "__main__":
    txt = input().rstrip()

    cnt = 0
    while len(txt) != 1:
        cnt += 1
        txt = sumup(txt)

    print(cnt)
    if txt in ['3', '6', '9']:
        print("YES")
    else:
        print("NO")
