"""
input :
5 8
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT

output :
TAAGATAC
7
"""
import sys
from collections import Counter

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    texts = list()
    for _ in range(N):
        texts.append(input().rstrip())
    texts_transposed = list(zip(*texts))

    # 개수 많은거 고름
    ans = list()
    for i in range(M):
        ans.append(sorted(Counter(texts_transposed[i]).most_common(), key=lambda x: (-x[1], x[0]))[0][0])
    for e in ans:
        print(e, end='')
    print()

    # get Hamming Distance
    tot = 0
    for i in range(N):
        tar = texts[i]
        for j in range(M):
            if tar[j] != ans[j]:
                tot += 1
    print(tot)
