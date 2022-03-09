import re
from collections import Counter


def diff(str1, str2):
    a = list(map(int, str1.split(',')))
    b = list(map(int, str2.split(',')))
    for key in Counter(b) - Counter(a):
        return key


def solution(s):
    splited = re.split('[{}]', s)

    augmented = []
    for ele in splited:
        if ele == '' or ele == ',':
            continue
        augmented.append(ele)

    if len(augmented) == 1:
        return [int(augmented[0])]

    augmented.sort(key=lambda x: len(x))
    ans = [int(augmented[0])]
    for i in range(len(augmented) - 1):
        ans.append(diff(augmented[i], augmented[i + 1]))

    return ans


if __name__ == "__main__":
    # 2 1 3 1
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
    # print(diff("2,3,1", "2,1,3,1"))
