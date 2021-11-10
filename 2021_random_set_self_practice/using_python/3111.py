"""
input :
banana
babananananadeda

output :
deda
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    pat = input().rstrip()
    txt = input().rstrip()
    pat_reverse = pat[::-1]

    f, r = 0, len(txt) - 1
    f_stk = []
    r_stk = []
    while f <= r:
        while f <= r:
            f_stk.append(txt[f])
            f += 1
            if len(f_stk) >= len(pat) and ''.join(f_stk[-len(pat):]) == pat:
                del f_stk[-len(pat):]
                break

        while f <= r:
            r_stk.append(txt[r])
            r -= 1
            if len(r_stk) >= len(pat) and ''.join(r_stk[-len(pat):]) == pat_reverse:
                del r_stk[-len(pat):]
                break

    stk_merged = f_stk + r_stk[::-1]
    idx = 0
    while idx >= 0:
        idx = ''.join(stk_merged).find(pat)
        if idx != - 1:
            del stk_merged[idx:idx + len(pat)]
    print(''.join(stk_merged))
