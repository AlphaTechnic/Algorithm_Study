def can_solve(n, times, K):
    tot = 0
    for time in times:
        tot += K // time
        if tot >= n:
            return True
    return False


def solution(n, times):
    times.sort()
    l = 1
    r = 10 ** 18
    mid_save = mid = (l + r) // 2
    while l <= r:
        if can_solve(n, times, mid):
            mid_save = mid
            r = mid - 1
            mid = (l + r) // 2
        else:
            l = mid + 1
            mid = (l + r) // 2
    return mid_save


if __name__ == "__main__":
    print(solution(10, [6, 8, 10]))
    # print(can_solve(6, [7, 10], 27))
