"""
input :
14
add 7
add 2
add 13
add 5
add 12
add 6
add 4
add 1
add 14
remove
add 10
remove
add 9
add 8
add 11
add 3
remove
remove
remove
remove
remove
remove
remove
remove
remove
remove
remove
remove

output :
3
"""
import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

if __name__ == "__main__":
    stk = []
    idx = 1
    cnt = 0

    N = int(input())
    for _ in range(2 * N):
        cmd = input().rstrip().split()
        if len(cmd) == 2:  # add
            num = int(cmd[1])
            stk.append(num)

        elif len(cmd) == 1:  # remove
            if len(stk) != 0 and stk[-1] != idx:  # miss남 => 재정렬
                cnt += 1
                stk.clear()
            elif len(stk) != 0 and stk[-1] == idx:  # hit
                stk.pop()

            idx += 1

    print(cnt)

