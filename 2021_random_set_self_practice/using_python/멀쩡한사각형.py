def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solution(a, b):
    return a * b - (a + b - gcd(a, b))


if __name__ == "__main__":
    print(solution(3, 5))
