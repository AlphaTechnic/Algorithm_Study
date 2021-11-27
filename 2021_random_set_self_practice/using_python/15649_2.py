"""
input :
4 2

output :
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


class Permutation(object):
    def __init__(self):
        self.N = self.M = -1
        self.chk = []

    def input(self):
        self.N, self.M = map(int, input().rstrip().split())
        self.chk = [False for _ in range(self.N + 1)]

    def recur(self, dep, ans):
        if dep == self.M:
            tmp = list(map(str, ans))
            print(' '.join(tmp))
            return

        for i in range(1, self.N + 1):
            if self.chk[i]: continue

            ans.append(i)
            self.chk[i] = True
            self.recur(dep + 1, ans)
            self.chk[i] = False
            ans.pop()


if __name__ == "__main__":
    permutation = Permutation()
    permutation.input()
    permutation.recur(0, [])
