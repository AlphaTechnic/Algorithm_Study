"""
input :
3 4
twice
9
jihyo
dahyeon
mina
momo
chaeyoung
jeongyeon
tzuyu
sana
nayeon
blackpink
4
jisu
lisa
rose
jenny
redvelvet
5
wendy
irene
seulgi
yeri
joy
sana
1
wendy
1
twice
0
rose
1

output :
twice
redvelvet
chaeyoung
dahyeon
jeongyeon
jihyo
mina
momo
nayeon
sana
tzuyu
blackpink
"""
import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

team2mem = defaultdict(list)
mem2team = defaultdict(str)

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    for _ in range(N):
        team_name = input().rstrip()
        mem_num = int(input())
        for _ in range(mem_num):
            mem_name = input().rstrip()
            team2mem[team_name].append(mem_name)
            mem2team[mem_name] = team_name
        team2mem[team_name].sort()

    for _ in range(M):
        name = input().rstrip()
        qt = int(input())
        if qt == 0:  # team이름 -> 멤버이름
            print('\n'.join(team2mem[name]))
        elif qt == 1:  # 멤버이름 -> 팀 이름
            print(mem2team[name])
