def add(list1, list2):
    ret_arr = [0 for _ in range(len(list1))]
    for i, (a, b) in enumerate(zip(list1, list2)):
        ret_arr[i] = a + b
    return ret_arr


def solution(arr1, arr2):
    ret = []
    for ele in list(zip(arr1, arr2)):
        list1, list2 = ele[0], ele[1]
        ret.append(add(list1, list2))

    return ret


if __name__ == "__main__":
    print(solution([[1], [2]], [[3], [4]]))
