CNT = 0


def dfs(numbers, target, pos, cur_val):
    global CNT
    if pos == len(numbers):
        if cur_val == target:
            CNT += 1
        return

    dfs(numbers, target, pos + 1, cur_val + numbers[pos])
    dfs(numbers, target, pos + 1, cur_val - numbers[pos])


def solution(numbers, target):
    global CNT
    dfs(numbers, target, 0, 0)
    return CNT


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))
