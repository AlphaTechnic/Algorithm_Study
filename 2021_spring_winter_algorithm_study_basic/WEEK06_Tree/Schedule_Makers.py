"""
input :
	  task의 cost, 일주일 간 널널한 정도, end date
업무 1 :    50
업무 2 :

HFS2001-01
HFS2002-01
MAT3020-01
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

task_cost_end = dict()  # 빅데이터프로그래밍 50 2020-06-02
time_spaces = []  # 100 100 80 20 100 100 100 20

task_cost_end['빅데이터프로그래밍'] = [50, 13]  # 13일 뒤
task_cost_end['시스템프로그래밍'] = [100, 14]  # 14일 뒤
task_cost_end['네트워크과제'] = [20, 7]  # 7일 뒤까지 가벼운 과제

for key in task_cost_end.keys():
    cost = task_cost_end[key][0]
    remaining_days = task_cost_end[key][1]
    task_cost_end[key].append(cost / remaining_days)

    print("%-10s : %s" % (key, task_cost_end[key][2]))
