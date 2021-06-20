"""
목적 :
여러 개의 작업 정보들(작업강도, 마감기한)이 있을 때, 오늘 나의 스케줄을 정리해주자.

input :
작업 강도, 마감 기한, 투자 시간

output :
Today's Schedule

우려사항 :
1. 수익모델 모르겠음. (배너광고, 광고 차단, 스티커 아이템 판매)
2. 가벼운 프로그램인 만큼 진입장벽 낮을 수 있음
3. 프론트 역할이 절대적 반응형으로 한다면, 백엔드가 필요 없을 수도
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

JOBS = dict()  # 빅데이터프로그래밍 50 2020-06-02
time_spaces = []  # 100 100 80 20 100 100 100 20

N = int(input())
for _ in range(N):
    job_name, d_day, intensity = input().split()
    d_day, intensity = map(int, [d_day, intensity])
    JOBS[job_name] = [d_day, intensity]

tot = 0
time_space = 8
for key in JOBS.keys():
    d_day = JOBS[key][0]
    cost = JOBS[key][1]
    JOBS[key].append(cost / d_day)

    tot += JOBS[key][2]

for key in JOBS.keys():
    print("%-15s : %.1f시간, 전체 작업의 %.1f%%"
          % (key, time_space * JOBS[key][2] / tot, JOBS[key][2]))

# merge, split 등 제공