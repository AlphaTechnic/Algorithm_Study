from collections import deque


class Priority2idx():
    def __init__(self, priority, idx):
        self.priority = priority
        self.idx = idx

    def __repr__(self):
        return f"(p:{self.priority}, idx:{self.idx})"


def can_popout(target, dq):
    for ele in dq:
        if ele.priority > target:
            return False
    return True


def solution(priorities, location):
    waiters = []
    for i, p in enumerate(priorities):
        waiters.append(Priority2idx(p, i))

    waiters_dq = deque(waiters)
    cnt = 0
    while True:
        if can_popout(waiters_dq[0].priority, list(waiters_dq)[1:]):
            ele = waiters_dq.popleft()
            cnt += 1
            if ele.idx == location:
                return cnt
        else:
            waiters_dq.rotate(-1)


if __name__ == "__main__":
    print(solution([2, 1, 3, 2], 2))
