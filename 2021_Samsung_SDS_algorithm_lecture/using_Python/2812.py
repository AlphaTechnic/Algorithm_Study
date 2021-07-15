"""
input :
10 4
4177252841

output :
775841
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())
    num = list(input())
    st = []
    cnt = K

    for i in range(N):
        while True:
            if cnt == 0: break
            if len(st) == 0: break

            if st[-1] < num[i]:
                st.pop()
                cnt -= 1
            else:
                break

        st.append(num[i])

    for digit in st[:N - K]:
        print(digit, end='')
