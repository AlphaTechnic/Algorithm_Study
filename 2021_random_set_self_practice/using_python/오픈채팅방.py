from collections import defaultdict


class User:
    def __init__(self, uid, nick):
        self.uid = uid
        self.nick = nick

    def change(self, nick):
        self.nick = nick


user_pool = defaultdict(lambda x: None)


def solution(record):
    seq = []
    for info in record:
        command = info.split()
        if command[0] == "Enter":
            uid = command[1]
            nick = command[2]

            user_pool[uid] = User(uid, nick)
            seq.append(("Enter", uid))

        elif command[0] == "Leave":
            uid = command[1]

            seq.append(("Leave", uid))

        elif command[0] == "Change":
            uid = command[1]
            nick = command[2]
            user_pool[uid].change(nick)

    ans = []
    for msg, uid in seq:
        if msg == "Enter":
            ans.append(f"{user_pool[uid].nick}님이 들어왔습니다.")
        if msg == "Leave":
            ans.append(f"{user_pool[uid].nick}님이 나갔습니다.")

    return ans


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo",
              "Change uid4567 Ryan"]
    print(solution(record))
