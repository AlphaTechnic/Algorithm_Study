"""
input :
3
2 B A
4 A B C D
2 A C

output :
A
--B
----C
------D
--C
B
--A
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


class Trie:
    head = dict()

    def add(self, txts):
        root = self.head
        for txt in txts:
            if txt in root:
                pass
            else:
                root[txt] = dict()
            root = root[txt]  # to next node
        root[0] = True  # end symbol

    @classmethod
    def dfs(cls, dep, root):
        if 0 in root: return

        curs = sorted(root)
        for cur in curs:
            print("--" * dep, end='')
            print(cur)
            Trie.dfs(dep + 1, root[cur])  # to next node


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        obj = Trie()
        obj.add(input().split()[1:])

    Trie.dfs(0, Trie.head)
