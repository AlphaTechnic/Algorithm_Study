from itertools import combinations


def mk_set(combi, columns):
    column_chosen = []
    for idx in combi:
        column_chosen.append(columns[idx])

    # mk set
    ret_set = set()
    for row in zip(*column_chosen):
        ret_set.add(row)
    return ret_set


def solution(relation):
    # 유일성 결정
    record_num = len(relation)
    columns = [col for col in zip(*relation)]
    column_num = len(columns)
    candidate_keys = list()
    for r in range(1, column_num + 1):
        combis = combinations([idx for idx in range(column_num)], r)
        for combi in combis:
            tmp_set = mk_set(combi, columns)
            if len(tmp_set) == record_num:
                candidate_keys.append(combi)

    # 최소성 결정
    ans = set(candidate_keys)
    for i in range(len(candidate_keys)):
        for j in range(i + 1, len(candidate_keys)):
            set1 = set(candidate_keys[i])
            set2 = set(candidate_keys[j])
            if set1.issubset(set2):
                ans.discard(candidate_keys[j])
    return len(ans)


if __name__ == "__main__":
    print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                    ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
    # print(solution([["a", "1", "aaa", "c", "ng"], ["a", "1", "bbb", "e", "g"], ["c", "1", "aaa", "d", "ng"],
    #                 ["d", "2", "bbb", "d", "ng"]]))
