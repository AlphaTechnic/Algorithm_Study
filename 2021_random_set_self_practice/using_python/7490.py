"""
input :
2
3
7

output :
1+2-3

1+2-3+4-5-6+7
1+2-3-4+5+6-7
1-2 3+4+5+6+7
1-2 3-4 5+6 7
1-2+3+4-5+6-7
1-2-3-4-5+6+7
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def cal(nums_or_op):
    st = [nums_or_op[0]]
    ind = 1
    while True:
        if nums_or_op[ind] == ' ':
            t = st.pop()
            st.append(int(str(t) + str(nums_or_op[ind + 1])))
            ind += 1
        else:
            st.append(nums_or_op[ind])
        ind += 1
        if ind >= len(nums_or_op):
            break

    if len(st) == 1:
        return st[0]

    # 계산
    res = st[0]
    ind = 1
    while True:
        if st[ind] == '+':
            res += st[ind + 1]
        elif st[ind] == '-':
            res -= st[ind + 1]
        ind += 2
        if ind >= len(st):
            break
    return res


def recur(i):
    if i == N - 1:
        if cal(tmp) == 0:
            ans_case = []
            for num in tmp:
                ans_case.append(num)
            ans.append(ans_case)
        return

    for op in ['+', '-', ' ']:
        tmp.append(op)
        tmp.append(nums[i + 1])
        recur(i + 1)
        tmp.pop()
        tmp.pop()


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())

        nums = [i for i in range(1, N + 1)]
        ans = list()
        tmp = [1]
        recur(0)

        ans.sort()
        for case in ans:
            for ele in case:
                print(ele, end='')
            print()
        print()
