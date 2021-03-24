import sys
sys.stdin = open("input.txt", "r")


from collections import deque
MAX = 100000

visited = [False for _ in range(MAX + 1)]

N, K = map(int, input().split())
ans = -1
queue = deque([(N, 0)])

while queue:
    i, cnt = queue.popleft()
    if i == K:
        ans = cnt
        break

    mul2 = 2 * i
    if mul2 != K and mul2 <= MAX:
        if visited[mul2] is False:
            queue.append((mul2, cnt + 1))
            visited[mul2] = True
    elif mul2 == K:
        ans = cnt + 1
        break

    plus1 = i + 1
    if plus1 != K and plus1 <= MAX:
        if visited[plus1] is False:
            queue.append((plus1, cnt + 1))
            visited[plus1] = True
    elif plus1 == K:
        ans = cnt + 1
        break

    minus1 = i - 1
    if minus1 != K and minus1 >= 0:
        if visited[minus1] is False:
            queue.append((minus1, cnt + 1))
            visited[minus1] = True
    elif minus1 == K:
        ans = cnt + 1
        break

print(ans)
