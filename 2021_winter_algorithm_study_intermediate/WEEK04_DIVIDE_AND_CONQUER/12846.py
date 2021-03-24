import sys
sys.stdin = open("input.txt", "r")

n = int(input())
pay_list = list(map(int, input().split()))
Sum = [0 for _ in range(100001)]
for i in range(n):
    if i == 0:
        t = 0
    else:
        t = Sum[i-1]
    Sum[i] += (pay_list[i] + t)


def get_max_profit(l, r):
    if l == r:
        return pay_list[l]
    m = (l+r) // 2
    res1 = get_max_profit(l, m)
    res2 = get_max_profit(m+1, r)
    min_val = min(pay_list[m], pay_list[m+1])
    sum = 2
    res3 = min_val*sum
    idx1 = m
    idx2 = m+1

    while l < idx1 and idx2 < r:
        if pay_list[idx1-1] < pay_list[idx2+1]:
            idx2+=1
            min_val = min(min_val, pay_list[idx2])
            sum += 1
        else:
            idx1 -=1
            min_val = min(min_val, pay_list[idx1])
            sum += 1

        res3 = max(res3, sum*min_val)

    while l < idx1:
        idx1-=1
        min_val = min(min_val, pay_list[idx1])
        sum += 1
        res3 = max(res3, sum*min_val)

    while r > idx2:
        idx2+=1
        min_val = min(min_val, pay_list[idx2])
        sum += 1
        res3 = max(res3, sum*min_val)

    return max(res1, max(res2, res3))


print(get_max_profit(0, n-1))

