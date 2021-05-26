"""
input :
3
1 2 3
1 3 2

output :
2 1 3
"""
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
inorder_nums = list(map(int, input().split()))
postorder_nums = list(map(int, input().split()))

pos = [0 for _ in range(N+1)]  # number의 inorder_nums 에서의 index
for i in range(N):
    pos[inorder_nums[i]] = i


def divide_and_conquer(in_s, in_e, post_s, post_e):
    # 종료 조건
    if in_s > in_e or post_s > post_e:
        return

    parents = postorder_nums[post_e]
    print(parents, end=" ")

    l_len = pos[parents] - in_s
    r_len = in_e - pos[parents]

    # 분할 정복
    divide_and_conquer(in_s, in_s + l_len - 1, post_s, post_s + l_len - 1)  # 왼쪽 서브트리
    divide_and_conquer(in_e - r_len + 1, in_e, post_e - r_len, post_e - 1)  # 오른쪽 서브트리


divide_and_conquer(0, N - 1, 0, N - 1)
