import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def preorder_to_postorder(start, end):
    if start > end:
        return

    divide = end + 1
    for i in range(start+1, end+1):
        if post[start] < post[i]:
            divide = i
            break
    preorder_to_postorder(start + 1, divide - 1)
    preorder_to_postorder(divide, end)
    print(post[start])


post = []
while True:
    try:
        number = int(input())
        post.append(number)
    except:
        break

preorder_to_postorder(0, len(post) - 1)