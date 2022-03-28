def solution(n, a, b):
    a += (n - 1)
    b += (n - 1)
    cnt = 0
    while a != b:
        a >>= 1
        b >>= 1
        cnt += 1
    return cnt


if __name__ == "__main__":
    print(solution(8, 4, 7))
