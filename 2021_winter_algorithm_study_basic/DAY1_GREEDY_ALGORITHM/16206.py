import sys

sys.stdin = open("input.txt", "r")

N, max_cut_num = tuple(map(int, input().split()))
rollcakes = list(map(int, input().split()))

cnt = 0
cut_num_stacked = 0
flag = 0
# for rollcake in rollcakes:
#     if flag == 0:
#         if rollcake % 10 == 0:
#             rollcake_num = int(rollcake / 10)
#             cut_num = rollcake_num - 1
#             cut_num_stacked += cut_num
#             if cut_num_stacked > max_cut_num:
#                 cut_num_stacked = cut_num_stacked - cut_num
#                 rollcake_num = max_cut_num - cut_num_stacked
#                 flag = 1
#
#         else:
#             rollcake_num = int(rollcake / 10)
#             if rollcake_num == 0:
#                 continue
#             cut_num = rollcake_num
#             cut_num_stacked += cut_num
#             if cut_num_stacked > max_cut_num:
#                 cut_num_stacked = cut_num_stacked - cut_num
#                 rollcake_num = max_cut_num - cut_num_stacked
#                 flag = 1
#         cnt += rollcake_num
#
#     else:
#         if rollcake == 10:
#             cnt += 1

# => 10의 배수인 롤케잌을 먼저 건드려야 되는 거였음!!!!!!!!!! 길이 10짜리 롤케잌을 얻는데에 자르는 횟수에서 이득을 보니까!!

filtered = []
for rollcake in rollcakes: # 자르지도 않고 얻는 롤케잌(길이 10짜리) 먼저 회수
    if rollcake == 10:
        cnt += 1
    elif rollcake < 10:
        continue
    else:
        filtered.append(rollcake)

filtered.sort() # => 이 와중에도 길이 20짜리 케잌을 먼저 건드려봐야하는 거였음!!!
filtered_2nd = []
for rollcake in filtered: # 자르는 횟수 대비 이득을 보는 길이 10의 배수짜리 롤케잌 회수
    if flag == 0:
        if rollcake % 10 == 0:
            rollcake_num = int(rollcake / 10)
            cut_num = rollcake_num - 1
            cut_num_stacked += cut_num
            if cut_num_stacked > max_cut_num:
                cut_num_stacked = cut_num_stacked - cut_num
                rollcake_num = max_cut_num - cut_num_stacked
                flag = 1
            cnt += rollcake_num
        else:
            filtered_2nd.append(rollcake)

        if flag == 1:
            break

if flag == 0: # 길이 10의 배수 아닌 롤케잌 회수
    for rollcake in filtered_2nd:
        rollcake_num = int(rollcake / 10)
        if rollcake_num == 0:
            continue
        cut_num = rollcake_num
        cut_num_stacked += cut_num
        if cut_num_stacked > max_cut_num:
            cut_num_stacked = cut_num_stacked - cut_num
            rollcake_num = max_cut_num - cut_num_stacked
            flag = 1
        cnt += rollcake_num

        if flag == 1:
            break

print(cnt)