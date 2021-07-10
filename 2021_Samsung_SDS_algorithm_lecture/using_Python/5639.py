"""
input :
50
30
24
5
28
45
98
52
60

output :
5
28
24
45
30
60
52
98
50
"""

import sys
sys.setrecursionlimit(10**8)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(l, r):
    # preorder[l] == 전위순회에서의 root
    if l > r:
        return

    border = l + 1
    for i in range(l + 1, r + 1):
        if preorder[i] > preorder[l]:
            border = i
            break

    recur(l + 1, border - 1)
    recur(border, r)
    print(preorder[l])


if __name__ == "__main__":
    preorder = []
    try:
        while True:
            preorder.append(int(input()))
    except:
        pass

    recur(0, len(preorder) - 1)
