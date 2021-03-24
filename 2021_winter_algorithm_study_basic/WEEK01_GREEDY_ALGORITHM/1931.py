import sys

sys.stdin = open("input.txt", "r")

conferences = []

N = int(input())
for _ in range(N):
    conference = list(map(int, input().split()))
    conferences.append(conference)

sorted_conferences = sorted(conferences, key=lambda x: (x[1], x[0]))
Min = sorted_conferences[0]

cnt = 1
# while True:
#     filtered = []
#     for candi in sorted_conferences[1:]:
#         if Min[1] <= candi[0]:
#             filtered.append(candi)
#     sorted_conferences = filtered
#     if not filtered:
#         break
#     Min = filtered[0]
#     cnt += 1

# O(n)으로 고침
for candi in sorted_conferences[1:]:
    if Min[1] > candi[0]:
        continue
    else:
        cnt += 1
        Min = candi



print(cnt)