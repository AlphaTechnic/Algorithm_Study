from collections import defaultdict


class User(object):
    def __init__(self, name, reporting=None):
        if reporting is None:
            reporting = set()
        self.name = name
        self.reporting = reporting

    def __repr__(self):
        return f"name-{self.name}"


class Pool(object):
    def __init__(self, users, threshold, id_list, reported=None):
        if reported is None:
            reported = defaultdict(set)
        self.id_list = id_list
        self.users = users
        self.threshold = threshold
        self.reported = reported
        self.punished = set()

    def mk_punished_users(self):
        for name, users_reporting in self.reported.items():
            if len(self.reported[name]) >= self.threshold:
                self.punished.add(name)

    def mk_mail(self):
        ret = []
        for id in self.id_list:
            cnt = 0
            for bad in self.punished:
                if bad in self.users[id].reporting:
                    cnt += 1
            ret.append(cnt)

        return ret


def solution(id_list, report, k):
    users = dict()
    for id in id_list:
        users[id] = User(id)

    pools = Pool(users=users, threshold=k, id_list=id_list)
    for info in report:
        a, b = info.split()
        users[a].reporting.add(b)
        pools.reported[b].add(a)
    pools.mk_punished_users()
    return pools.mk_mail()


if __name__ == "__main__":
    print(solution(["muzi", "frodo", "apeach", "neo"],
                   ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
