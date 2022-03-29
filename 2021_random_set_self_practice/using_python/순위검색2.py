from collections import defaultdict
from itertools import combinations


class ApplicantPool:
    Pool = defaultdict(list)

    def push(self, fields):
        language, job_grp, career, soul_food, score = fields
        # self.Pool[(language, job_grp, career, soul_food)].append(score)

        to_push = [language, job_grp, career, soul_food]
        for r in range(len(to_push) + 1):
            for combi in combinations([i for i in range(len(to_push))], r):
                language, job_grp, career, soul_food = self.mk_to_push(to_push, combi)
                self.Pool[(language, job_grp, career, soul_food)].append(score)

    def mk_to_push(self, to_push, combi):
        ret = []
        for i, elem in enumerate(to_push):
            if i in combi:
                ret.append('-')
            else:
                ret.append(elem)
        return ret

    def sort_score(self):
        for key, value in self.Pool.items():
            value.sort()

    def how_many(self, condition):
        language, job_grp, career, soul_food, score = condition
        if (language, job_grp, career, soul_food) in self.Pool:
            scores = self.Pool[(language, job_grp, career, soul_food)]
            idx = self.find_idx_using_binary_search(scores, score)
            return len(scores) - idx
        else:
            return 0

    @staticmethod
    def find_idx_using_binary_search(arr, tar):
        l = 0
        r = len(arr)
        mid_save = mid = (l + r) // 2

        arr.append(10 ** 9)
        while l <= r:
            if tar <= arr[mid]:
                mid_save = mid
                r = mid - 1
                mid = (l + r) // 2
            else:
                l = mid + 1
                mid = (l + r) // 2
        arr.pop()
        return mid_save


def solution(info, query):
    pool = ApplicantPool()

    for raw in info:
        language, job_grp, career, soul_food, score = raw.split()
        fields = [language, job_grp, career, soul_food, int(score)]
        pool.push(fields)
    pool.sort_score()

    ans = []
    for raw in query:
        language, job_grp, career, raw2 = raw.split(' and ')
        soul_food, score = raw2.split()
        condition = (language, job_grp, career, soul_food, int(score))
        ans.append(pool.how_many(condition))
    return ans


if __name__ == "__main__":
    print(solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]))
