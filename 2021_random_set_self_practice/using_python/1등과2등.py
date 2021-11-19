"""
input :
213412

output :
Yes
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

chk = {"12": [], "21": []}

if __name__ == "__main__":
    txt = input().rstrip()

    idx = 1
    while idx < len(txt):
        if txt[idx - 1] == '1' and txt[idx] == '2':
            chk["12"].append((idx - 1, idx))
        elif txt[idx - 1] == '2' and txt[idx] == '1':
            chk["21"].append((idx - 1, idx))
        idx += 1

    for i in range(len(chk["12"])):
        for j in range(len(chk["21"])):
            a, b = chk["12"][i]
            c, d = chk["21"][j]
            if a != b and a != d and b != c and b != d:
                print("Yes")
                exit(0)
    print("No")
