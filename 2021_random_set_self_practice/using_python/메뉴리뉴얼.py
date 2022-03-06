from itertools import combinations
from collections import Counter


def solution(orders, course):
    ret = []
    for course_size in course:
        combis = []
        for order in orders:
            combis.extend(list(combinations(sorted(list(order)), course_size)))
        counter = Counter(combis).most_common()

        ans = list(filter(lambda x: x[1] == counter[0][1] and x[1] >= 2, counter))
        for ele, _ in ans:
            ret.append(''.join(sorted(list(ele))))
    return sorted(ret)


if __name__ == "__main__":
    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
