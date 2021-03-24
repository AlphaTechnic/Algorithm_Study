import sys
import re
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

input()
expr = input().replace(' ', '')

muls = list(map(lambda x: int(x[1]), re.findall(r'\*[0-9]', expr)))
divs = list(map(lambda x: int(x[1]), re.findall(r'\/[0-9]', expr)))

ans = 1
for num in muls:
    ans *= num
for num in divs:
    ans /= num

if ans.is_integer():
    print("mint chocolate")
else:
    print("toothpaste")