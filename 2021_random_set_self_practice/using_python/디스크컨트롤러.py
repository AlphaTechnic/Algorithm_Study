class Task:
    def __init__(self, arrive_time, length):
        self.arrive_time = arrive_time
        self.length = length

        self.exec_start_time = self.arrive_time
        self.exec_end_time = self.exec_start_time + self.length

    def push_backward(self, start_time):
        self.exec_start_time = start_time
        self.exec_end_time = self.exec_start_time + self.length

    def __repr__(self):
        return f"arrive:{self.arrive_time}, length:{self.length}"


def solution(jobs):
    tasks = []
    for arrive_time, length in jobs:
        tasks.append(Task(arrive_time, length))

    tot = 0
    while tasks:
        tasks.sort(key=lambda t: (t.exec_start_time, t.length))
        for task in tasks[1:]:
            if task.exec_start_time < tasks[0].exec_end_time:
                task.push_backward(tasks[0].exec_end_time)
            else:
                break
        first = tasks.pop(0)
        tot += first.exec_end_time - first.arrive_time
    return tot // len(jobs)


if __name__ == "__main__":
    print(solution([[0, 3], [1, 9], [2, 6]]))
