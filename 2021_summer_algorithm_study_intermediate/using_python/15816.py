"""
input :
3
1 10 20
4
2 1 20
1 5
2 1 20
2 1 1

output:
17
16
0
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

PIV = 1 << 22
tree = [0 for _ in range(2 * PIV)]


def update(x):
    global PIV
    x += PIV
    if tree[x]: return

    tree[x] += 1
    while True:
        x >>= 1
        if x == 0: return
        tree[x] += 1


def query(l, r):
    global PIV
    l += PIV;
    r += PIV;

    ret = 0
    while l <= r:
        if l & 1:
            ret += tree[l]
            l += 1
        if not (r & 1):
            ret += tree[r]
            r -= 1
        l >>= 1;
        r >>= 1;
    return ret


if __name__ == "__main__":
    N = int(input())
    init_updates = list(map(int, input().rstrip().split()))
    cmds = []
    nums = []
    for num in init_updates:
        nums.append(num)

    # query들을 미리 전처리
    M = int(input())
    for _ in range(M):
        line = list(map(int, input().rstrip().split()))
        cmds.append(line)
        if line[0] == 1:
            nums.append(line[1])
        else:
            nums.append(line[1])
            nums.append(line[2])

    # 좌표 압축
    nums = list(set(nums))
    nums.sort()
    Q2I = dict()
    for ind, q in enumerate(nums):
        Q2I[q] = ind

    # 미리 주어진 update 쿼리 처리
    for num in init_updates:
        update(Q2I[num])

    # cmd 시퀀스를 다시 하나씩 보면서, 업데이트 쿼리와 구간합 쿼리를 수행
    for cmd in cmds:
        if cmd[0] == 1:
            x = cmd[1]
            update(Q2I[x])
        elif cmd[0] == 2:
            l, r = cmd[1], cmd[2]

            tot = query(Q2I[l], Q2I[r])
            print(r - l + 1 - tot)
