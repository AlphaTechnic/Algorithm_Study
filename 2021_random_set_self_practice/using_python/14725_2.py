import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(dep, root):
    curs = sorted(root)
    for cur in curs:
        print('--' * dep, cur, sep='')
        dfs(dep + 1, root[cur])  # to next node


if __name__ == "__main__":
    ROOT = dict()
    N = int(input())

    for _ in range(N):
        txts = input().split()[1:]
        cur = ROOT
        for txt in txts:
            if txt in cur:
                pass
            else:
                cur[txt] = dict()
            cur = cur[txt]

    dfs(0, ROOT)
