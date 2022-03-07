from collections import defaultdict
from collections import Counter


def union_counter(counter1, counter2):
    dic = defaultdict(int)
    for key, num in counter1.items():
        dic[key] += num
    for key, num in counter2.items():
        dic[key] = max(dic[key], num)

    tot = 0
    for _, num in dic.items():
        tot += num
    return tot


def intersect_counter(counter1, counter2):
    dic = defaultdict(int)
    for key, num in counter1.items():
        if key in counter2:
            dic[key] += num
    for key, num in counter2.items():
        if key in counter1:
            dic[key] = min(dic[key], num)

    tot = 0
    for _, num in dic.items():
        tot += num
    return tot


def solution(str1, str2):
    list1 = []
    for i in range(len(str1) - 1):
        tar = f"{str1[i]}{str1[i + 1]}"
        if not tar.isalpha():
            continue
        list1.append(tar.lower())
    list2 = []
    for i in range((len(str2) - 1)):
        tar = f"{str2[i]}{str2[i + 1]}"
        if not tar.isalpha():
            continue
        list2.append(tar.lower())
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    denominator = union_counter(counter1, counter2)
    if denominator == 0:
        return 65536
    numerator = intersect_counter(counter1, counter2)
    return int(65536 * (numerator / denominator))


if __name__ == "__main__":
    print(solution("FRANCE", "french"))
