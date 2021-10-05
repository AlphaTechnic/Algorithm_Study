"""
input :
5
ICPC
ACM
CONTEST
GCPC
PROGRAMM

3
ACMA
APCA
TOGI
NEST

PCMM
RXAI
ORCN
GPCG

ICPC
GCPC
ICPC
GCPC

output :
8 CONTEST 4
14 PROGRAMM 4
2 GCPC 2
"""
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

direction = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))


def update(txt, score, longest, found):
    # score
    if len(txt) == 3 or len(txt) == 4:
        score += 1
    elif len(txt) == 5:
        score += 2
    elif len(txt) == 6:
        score += 3
    elif len(txt) == 7:
        score += 5
    elif len(txt) == 8:
        score += 11

    # longest
    if len(txt) > len(longest):
        longest = txt
    elif len(txt) == len(longest):
        if txt < longest:
            longest = txt

    # found
    found += 1

    return score, longest, found


def dfs(cy, cx, find_set, seq, dep):
    if dep == 8:
        return

    global score, longest, found
    vis[cy][cx] = True
    seq.append(bd[cy][cx])

    res = ''.join(seq)
    if res in words:
        if res not in find_set:
            find_set.add(res)
            score, longest, found = update(res, score, longest, found)

    for dy, dx in direction:
        ny, nx = cy + dy, cx + dx
        if not (0 <= ny < 4 and 0 <= nx < 4): continue
        if vis[ny][nx]: continue

        dfs(ny, nx, find_set, seq, dep + 1)

    vis[cy][cx] = False
    seq.pop()


if  __name__ == "__main__":
    words = set()
    N = int(input())
    for _ in range(N):
        words.add(input().rstrip())
    input()

    T = int(input())
    for _ in range(T):
        # init
        score = 0
        longest = ""
        found = 0
        bd = [list(input().rstrip()) for _ in range(4)]
        find_set = set()

        for r in range(4):
            for c in range(4):
                vis = [[False for _ in range(4)] for _ in range(4)]
                dfs(r, c, find_set, [], 0)

        print(score, longest, found)

        input()
