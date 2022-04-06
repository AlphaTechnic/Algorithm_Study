from datetime import datetime, timedelta
from collections import deque
from typing import List


class Bus(object):
    def __init__(self, arrive_time: datetime, capacity: int):
        self.arrive_time = arrive_time
        self.capacity = capacity

    def __repr__(self):
        return f"{self.arrive_time.hour}:{self.arrive_time.minute}/{self.capacity}"


class Person(object):
    def __init__(self, arrive_time: datetime):
        self.arrive_time = arrive_time

    def __repr__(self):
        return f"{self.arrive_time.hour}:{self.arrive_time.minute}"


class ManagingMachine(object):
    def __init__(self, buses: List[Bus], people: List[Person]):
        self.buses = buses
        self.people = deque(people)
        self.processed_num = 0
        self.last_served_person = None

    def sweep_away(self):
        for bus in self.buses:
            try:
                self.get_on_the_bus(bus)
            except:
                # 모든 사람들 serving 완료
                return self.ret_answer()
        return self.ret_answer()

    def get_on_the_bus(self, bus):
        self.processed_num = 0
        for _ in range(bus.capacity):
            if self.people[0].arrive_time <= bus.arrive_time:
                person = self.people.popleft()
                self.processed_num += 1
                self.last_served_person = person
            else:
                break

    def ret_answer(self):
        if self.last_served_person is None:
            return self.buses[-1].arrive_time

        if self.processed_num == self.buses[0].capacity:
            # 버스가 딱 떨어지게 서비스 함
            return self.last_served_person.arrive_time - timedelta(minutes=1)
        # 버스에 남은 자리가 있었음
        return self.buses[-1].arrive_time


def solution(n, t, m, timetable):
    buses = []
    dt = datetime.strptime("09:00", "%H:%M")
    for _ in range(n):
        buses.append(Bus(dt, m))
        dt += timedelta(minutes=t)

    timetable.sort()
    people = []
    for time_str in timetable:
        people.append(Person(datetime.strptime(time_str, "%H:%M")))

    machine = ManagingMachine(buses, people)
    dt = machine.sweep_away()
    return datetime.strftime(dt, "%H:%M")


if __name__ == "__main__":
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
    print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
    print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
    print(solution(1, 1, 1, ["23:59"]))
    print(solution(10, 60, 45,
                   ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                    "23:59", "23:59", "23:59", "23:59", "23:59"]))
