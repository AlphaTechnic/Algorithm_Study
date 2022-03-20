# 이제는 할 수 있을 듯

def calc(t, s):
    length = len(s)
    ans = 0
    if t == 0:
        for i in range(length - 1, -1, -1):
            if s[i] != 'A':
                ans = i
                break
        return ans
    if t == 1:
        for i in range(1, length):
            if s[i] != 'A':
                ans = length - i
                break
        return ans
    if t == 2:
        mid = (length - 1) // 2
        for i in range(mid - 1, -1, -1):
            if s[i] != 'A':
                ans += (mid - i) * 2
                break
        for i in range(mid, length):
            if s[i] != 'A':
                ans += (length - i + 1)
                break
    if t == 3:
        mid = (length - 1) // 2
        for i in range(mid, length):
            if s[i] != 'A':
                ans += (length - i) * 2
                break
        for i in range(mid - 1, -1, -1):
            if s[i] != 'A':
                ans += i
                break
    return ans


def solution(s):
    ud_value = 0
    for ch in s:
        if ch != 'A':
            a = ord(ch) - ord('A')
            b = ord('Z') - ord(ch) + 1
            ud_value += min(a, b)

    if all(ch == 'A' for ch in s):
        return ud_value

    lr_value = len(s) - 1
    for i in range(4):
        a = min(lr_value, calc(i, s))
        lr_value = a

    return lr_value + ud_value


if __name__ == "__main__":
    print(solution("JEROEN"))
