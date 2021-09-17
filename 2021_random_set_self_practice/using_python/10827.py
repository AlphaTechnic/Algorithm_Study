"""
input :
3.141592 3

output :
31.006257328285746688
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    a, b = map(list, input().rstrip().split())

    flag = False
    cnt = 0
    for i, ch in enumerate(a):
        if ch == '.':
            del a[i]
            flag = True
        if flag:
            cnt += 1

    ans = list(str(int(''.join(a)) ** int(''.join(b))))
    ans = ['0'] * 91 + ans

    tune = cnt * int(''.join(b))
    ans.insert(- tune, '.')

    for i, ch in enumerate(ans):
        if ans[i + 1] == '.' or ans[i] != '0':
            ans = ans[i:]
            break
    print(''.join(ans))
