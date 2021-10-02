"""
input :
2
3
Yonsei 10
Korea 10000000
Ewha 20
2
Yonsei 1
Korea 10000000

output :
Korea
Korea
"""
import sys
from collections import defaultdict
from collections import Counter

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        chk = defaultdict(int)
        for _ in range(N):
            name, nm = input().rstrip().split()
            chk[name] += int(nm)
        print(Counter(chk).most_common()[0][0])
