from collections import deque


def solution(n):
    ans = deque()
    while n != 0:
        piv = n % 3
        if piv == 0:
            ans.appendleft(4)
            n = n // 3 - 1
        else:
            ans.appendleft(piv)
            n //= 3
    return ''.join(map(str, ans))


if __name__ == "__main__":
    print(solution(12))
