"""
input :
5
GOOD
LUCK
AND
HAVE
FUN
7

output :
31YUB
"""
import sys
from collections import deque
from collections import defaultdict
from collections import Counter

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

ch2quant = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
    'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
    'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
    'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
    'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34,
    'Z': 35
}
quant2ch = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
    15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J',
    20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O',
    25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T',
    30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y',
    35: 'Z'
}


def to36(dec):
    if dec == 0: return '0'

    res = deque()
    while dec != 0:
        dec, r = dec // 36, dec % 36
        res.appendleft(quant2ch[r])
    return ''.join(res)


dig2poten = defaultdict(int)

if __name__ == "__main__":
    N = int(input())

    tot = 0
    for _ in range(N):
        txt = input().rstrip()
        p = 0
        for i in range(len(txt) - 1, -1, -1):
            dig2poten[txt[i]] += (ch2quant['Z'] - ch2quant[txt[i]]) * 36 ** p
            tot += ch2quant[txt[i]] * 36 ** p
            p += 1
    K = int(input())

    counter = Counter(dig2poten).most_common()
    for i in range(min(K, len(counter))):
        tot += counter[i][1]

    print(to36(tot))
