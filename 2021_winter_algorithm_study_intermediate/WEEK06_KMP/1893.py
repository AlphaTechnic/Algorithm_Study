import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(T):
    ans = []
    A = list(input())
    W = list(input())
    S = list(input())
    ind = [0] * 128
    for i in range(len(A)):
        ind[ord(A[i])] = i

    for k in range(len(A)):
        cnt = 0
        fail = [0]*len(W)
        for i in range(1, len(W)):
            j = 0
            while j > 0 and W[i] != W[j]:
                j = fail[j-1]
            if W[i] == W[j]:
                j += 1
                fail[i] = j

        for i in range(len(S)):
            while j > 0 and S[i] != W[j]:
                j = fail[j-1]
            if S[i] == W[j]:
                if j == len(W)-1:
                    j = fail[j]
                    cnt += 1
                    if cnt > 1:
                        break
                else:
                    j += 1

        if cnt == 1:
            ans.append(k)

        for i in range(len(W)):
            W[i] = A[(ind[ord(W[i])] + 1) % len(A)]

    if len(ans) == 0:
        print("no solution", end='')
    elif len(ans) == 1:
        print("unique: ", end='')
        for i in ans:
            print(i, end=' ')
        print('')
    else:
        print("ambiguous: ", end='')
        for i in ans:
            print(i, end=' ')
        print('')

