"""
input :
mirkovC4nizCC44
C4

output :
mirkovniz
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    txt = input().rstrip()
    pat = input().rstrip()

    st = []
    f, e = 0, len(txt) - 1
    while f <= e:
        while f <= e:
            st.append(txt[f])
            f += 1
            if len(st) >= len(pat) and st[-1] == pat[-1] and ''.join(st[-len(pat):]) == pat:
                del st[-len(pat):]
                break

    if len(st) != 0:
        print(''.join(st))
    else:
        print("FRULA")
