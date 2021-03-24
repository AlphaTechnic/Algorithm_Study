import sys
sys.stdin = open("input.txt", "r")



def fibo(ind):
    a = [[0, 0], [0, 0]]
    b = [[0, 0], [0, 0]]
    c = [[0, 0], [0, 0]]

    if ind == 1:
        a[0][0] = 1
        a[0][1] = 1
        a[1][0] = 1
        a[1][1] = 0
    elif ind%2 == 1:
        b = fibo(ind - 1)
        c = fibo(1)
        a[0][0] = (b[0][0] * c[0][0] + b[0][1] * c[1][0]) % 10000
        a[0][1] = (b[0][0] * c[0][1] + b[0][1] * c[1][1]) % 10000
        a[1][0] = (b[1][0] * c[0][0] + b[1][1] * c[1][0]) % 10000
        a[1][1] = (b[1][0] * c[0][1] + b[1][1] * c[1][1]) % 10000
    else: # ind가 짝수
        b = fibo(ind // 2)
        a[0][0] = (b[0][0] * b[0][0] + b[0][1] * b[1][0]) % 10000
        a[0][1] = (b[0][0] * b[0][1] + b[0][1] * b[1][1]) % 10000
        a[1][0] = (b[1][0] * b[0][0] + b[1][1] * b[1][0]) % 10000
        a[1][1] = (b[1][0] * b[0][1] + b[1][1] * b[1][1]) % 10000

    return a

ind_list = []
while True:
    ind = int(input())
    if ind == -1:
        break
    else:
        ind_list.append(ind)

for ind in ind_list:
    if ind == 0:
        print(0)
    else:
        mat = fibo(ind)
        print(mat[0][1])

