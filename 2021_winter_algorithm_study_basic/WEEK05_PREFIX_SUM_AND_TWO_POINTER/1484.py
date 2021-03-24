import sys
sys.stdin = open("input.txt", "r")

G = int(input()) # G = 현재몸무게^2 - 기억하는몸무게^2

square_list = [i*i for i in range(200001)]

ans = []
a = b = 1
while b <= 200000:
    dif = square_list[b] - square_list[a]
    if dif < G:
        b += 1
    elif dif > G:
        a += 1
    else: # sum_of_intervals == G
        ans.append(b)
        b += 1

if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)