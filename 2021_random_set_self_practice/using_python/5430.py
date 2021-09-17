"""
input :
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]

output :
[2,1]
error
[1,2,3,5,8]
error
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def get_num_of_R(funs):
    cnt = 0
    for fun in funs:
        if fun == 'R':
            cnt += 1
    return cnt


def optimize_funs(funs):
    g_val = 0
    for i, fun in enumerate(funs):
        if fun == 'R':
            if g_val == 0:
                chk[i] = -1
                g_val = -1
            elif g_val == -1:
                chk[i] = 0
                g_val = 0
        else:
            chk[i] = g_val


if __name__ == "__main__":
    T = int(input())

    try:
        while True:
            for _ in range(T):
                funs = input().rstrip()
                N = int(input())

                # N == 0 인 edge case 처리
                if N == 0:
                    if 'D' in funs:
                        print("error")
                    else:
                        print("[]")
                    input()
                    continue

                # funs 전처리
                deq = deque(map(int, input().rstrip()[1:-1].split(',')))
                chk = [0 for _ in range(len(funs))]
                optimize_funs(funs)
                R_num = get_num_of_R(funs)

                # 함수 sequence 수행
                try:
                    for i, fun in enumerate(funs):
                        if fun == 'D':
                            if chk[i] == 0:
                                deq.popleft()
                            else:
                                deq.pop()
                except:
                    print("error")
                    continue

                # print ans
                if R_num & 1:
                    deq.reverse()
                deq = list(map(str, deq))
                print('[' + ','.join(deq) + ']')

    except:
        # intentional fall through
        pass
