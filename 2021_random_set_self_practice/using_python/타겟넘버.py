cnt = 0


def dfs(numbers, target, pos, cur_val):
    global cnt
    if pos == len(numbers):
        if cur_val == target:
            cnt += 1
        return

    dfs(numbers, target, pos + 1, cur_val + numbers[pos])
    dfs(numbers, target, pos + 1, cur_val - numbers[pos])


def solution(numbers, target):
    global cnt
    dfs(numbers, target, 0, 0)
    return cnt


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))
