"""
input :
10 9
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9
1 10
2 3 10
1 4

output :
4
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, P = map(int, input().rstrip().split())
    tmans = list(map(int, input().rstrip().split()))
    if len(tmans) == 1:
        print(P)
        exit(0)

    tmans.pop(0)
    tmans = set(tmans)

    parties = []
    for _ in range(P):
        party = list(map(int, input().rstrip().split()))
        party.pop(0)
        parties.append(party)
    chk = [False for _ in range(P)]

    while True:
        SZ_save = len(tmans)
        for i, party in enumerate(parties):
            for mem in party:
                if (not chk[i]) and mem in tmans:
                    tmans = tmans.union(set(party))
                    chk[i] = True
                    break
        if SZ_save == len(tmans):
            break

    cnt = 0
    for i in range(len(chk)):
        if not chk[i]:
            cnt += 1
    print(cnt)
