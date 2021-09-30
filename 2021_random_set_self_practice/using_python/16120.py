"""
input :
PPPAPAP

output :
PPAP
"""
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline


def is_ppap(txt):
    if txt == 'P':
        return True
    if 'A' not in txt:
        return False

    p_cnt = 0
    ind = 0
    while ind < len(txt):
        if txt[ind] == 'P':
            p_cnt += 1
            ind += 1
        else:
            if p_cnt >= 2 and ind + 1 < len(txt) and txt[ind + 1] == 'P':
                p_cnt -= 1
                ind += 2
            else:
                return False
    return True


if __name__ == "__main__":
    txt = input().rstrip()
    if is_ppap(txt):
        print("PPAP")
    else:
        print("NP")
