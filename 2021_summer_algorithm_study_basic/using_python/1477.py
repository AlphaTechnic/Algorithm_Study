"""
input :
6 7 800
622 411 201 555 755 82

output :
70
"""
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

if __name__ == "__main__":
    N, M, L = map(int, input().rstrip().split())
    poses = list(map(int, input().rstrip().split()))
    poses += [0, L]
    poses.sort()

    N += 1

    l = 0
    r = L
    mid_save = mid = (l + r) // 2
    while l <= r:
        tot = 0
        for i in range(1, len(poses)):
            tot += (poses[i] - poses[i - 1] - 1) // mid

        if tot <= M:
            mid_save = mid
            r = mid - 1
            mid = (l + r) // 2
        else:
            l = mid + 1
            mid = (l + r) // 2

    print(mid_save)