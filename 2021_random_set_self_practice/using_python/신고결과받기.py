class User(object):
    def __init__(self, name, report=None):
        if report is None:
            report = set()
        self.name = name
        self.report = report


class Pool(object):
    def __init__(self, users, reports=None):
        if reports is None:
            reports = dict()
        self.users = users
        self.reports = reports


def solution(id_list, report, k):
    users = dict()
    for id in id_list:
        users[id] = User(id)
    pools = Pool(users=set(id_list))
    for info in report:
        a, b = info.split()
        users[a].report.add(b)
        pools.reports[a] = b

    return answer


if __name__ == "__main__":
    print(solution(["muzi", "frodo", "apeach", "neo"],
                   ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]))
