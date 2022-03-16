"""
input :
4
2 1 1 0

output:
4 2 1 3
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


class Person:
    def __init__(self, height=-1, taller_on_left=-1):
        self.height = height
        self.taller_on_left = taller_on_left

    def __repr__(self):
        return f"h:{self.height} on_left:{self.taller_on_left}"


if __name__ == "__main__":
    N = int(input())
    on_left = list(map(int, input().rstrip().split()))

    people = []
    for i in range(len(on_left)):
        people.append(Person(i, on_left[i]))

    people.sort(key=lambda x: x.height, reverse=True)

    stand = []
    for person in people:
        stand.insert(person.taller_on_left, person)
    for p in stand:
        print(p.height + 1, end=' ')
    print()
