"""
input :
3
1 2 3
1 3 2

output :
2 1 3


7
4 2 5 1 6 3 7
4 5 2 6 7 3 1
"""
import sys
sys.setrecursionlimit(10 ** 8)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(in_l, in_r, post_l, post_r):
    if in_l > in_r: return
    if post_l > post_r: return

    nd = postorder[post_r]
    ans.append(nd)

    l_tree_sz = poses[nd] - in_l
    r_tree_sz = in_r - poses[nd]
    recur(in_l, in_l + l_tree_sz - 1, post_l, post_l + l_tree_sz - 1)
    recur(poses[nd] + 1, (poses[nd] + 1) + (r_tree_sz - 1), (post_r - 1) - (r_tree_sz - 1), post_r - 1)


if __name__ == "__main__":
    N = int(input())
    inorder = list(map(int, input().rstrip().split()))
    postorder = list(map(int, input().rstrip().split()))

    poses = [-1 for _ in range(N + 1)]
    for i, nd in enumerate(inorder):
        poses[nd] = i

    ans = []
    recur(0, N - 1, 0, N - 1)
    for num in ans:
        print(num, end=' ')
