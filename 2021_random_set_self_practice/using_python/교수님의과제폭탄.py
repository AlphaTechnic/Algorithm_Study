"""
input :
8
1/1 12/31
1/2 12/30
1/3 12/29
1/4 12/28
1/5 12/27
1/6 12/26
1/7 12/25
1/8 12/24

output :
Yes
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def chk_paren(txt):
    stk = []
    for _, k in txt:
        if k > 0:
            stk.append(k)
        else:
            if len(stk) == 0:
                return False

            if k == - stk[-1]:
                stk.pop()
            else:
                return False
    if len(stk) != 0:
        return False

    return True


if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print("Yes")
        exit(0)

    seq = []
    for _ in range(N):
        s, e = input().rstrip().split()
        s, e = list(map(int, s.split('/'))), list(map(int, e.split('/')))
        s, e = s[0] * 100 + s[1], e[0] * 100 + e[1]
        seq.append((s, e))
    seq.sort(key=lambda x: (x[0], -x[1]))

    txt = []
    for i, (s, e) in enumerate(seq, start=1):
        txt.append((s, i))
        txt.append((e, -i))
    txt.sort()

    # 괄호 검사
    if chk_paren(txt):
        print("Yes")
    else:
        print("No")
