"""
input :
baaa

output :
A
"""

import sys
import collections
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

string = input().rstrip().upper()
if len(string) == 1:
    print(string)
    exit()

count_info = collections.Counter(string).most_common()
if count_info[0][1] == count_info[1][1]:
    print("?")
else:
    print(count_info[0][0])