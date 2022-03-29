class Applicant:
    def __init__(self, language, job_grp, career, soul_food, score):
        self.language = language
        self.job_grp = job_grp
        self.career = career
        self.soul_food = soul_food
        self.score = score

    def __repr__(self):
        return f"{self.language}/{self.score}"


def is_corresponded(applicant, conditions):
    language, job_grp, career, soul_food, score = conditions
    if language != '-' and applicant.language != language:
        return False
    if job_grp != '-' and applicant.job_grp != job_grp:
        return False
    if career != '-' and applicant.career != career:
        return False
    if soul_food != '-' and applicant.soul_food != soul_food:
        return False
    if applicant.score < score:
        return False
    return True


def how_many(applicants, conditions):
    cnt = 0
    for applicant in applicants:
        if is_corresponded(applicant, conditions):
            cnt += 1
    return cnt


def solution(info, query):
    applicants = []
    for raw in info:
        language, job_grp, career, soul_food, score = raw.split()
        applicants.append(Applicant(language, job_grp, career, soul_food, int(score)))

    ans = []
    for raw in query:
        language, job_grp, career, raw2 = raw.split(' and ')
        soul_food, score = raw2.split()
        conditions = [language, job_grp, career, soul_food, int(score)]
        ans.append(how_many(applicants, conditions))
    return ans


if __name__ == "__main__":
    print(solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]))
