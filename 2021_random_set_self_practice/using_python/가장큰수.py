class Number():
    def __init__(self, s):
        self.s = s

    def __lt__(self, other):
        if self.s + other.s < other.s + self.s:
            return True
        return False

    def __repr__(self):
        return self.s


def solution(numbers):
    numbers = list(map(str, numbers))
    customized_numbers = []
    for num in numbers:
        customized_numbers.append(Number(num))
    customized_numbers.sort(reverse=True)

    ans = ""
    for num_obj in customized_numbers:
        ans += num_obj.s

    if eval(ans) == 0:
        return '0'
    return ans


if __name__ == "__main__":
    print(solution([0, 0, 0, 0]))
    # print(solution([3, 30, 34, 5, 9]))
    # "9534330"
