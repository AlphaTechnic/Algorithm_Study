from datetime import datetime, timedelta
from typing import List

Tune = timedelta(seconds=0.001)


class Log(object):
    def __init__(self, end: datetime, length: timedelta):
        self.end = end
        self.length = length
        self.start = self.end - length + Tune


class LogAnalyzer(object):
    def __init__(self, logs: List[Log]):
        self.logs = logs

    def get_max_throughput_per_second(self):
        max_val = -1
        for i, log in enumerate(self.logs):
            start, end = self.set_interval(log)
            cnt = self.how_many_in_interval(self.logs[i:], [start, end])
            max_val = max(max_val, cnt)
        return max_val

    def set_interval(self, log) -> List[datetime]:
        return [log.end, log.end + timedelta(seconds=1) - Tune]

    def how_many_in_interval(self, logs, interval):
        cnt = 0
        for log in logs:
            if self.is_in_interval(log, interval):
                cnt += 1
        return cnt

    def is_in_interval(self, log, interval):
        start, end = interval
        return not (end < log.start or start > log.end)


def mk_logs(lines):
    logs = []
    for line in lines:
        date, time, raw3 = line.split()
        end = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S.%f")
        length = timedelta(seconds=float(raw3.split('s')[0]))
        logs.append(Log(end, length))
    return logs


def solution(lines):
    logs = mk_logs(lines)
    return LogAnalyzer(logs).get_max_throughput_per_second()


if __name__ == "__main__":
    print(solution(lines=["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
    # print(solution(lines=["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"]))
